from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load a lightweight sentence transformer (we will use a minimal model or fallback to exact match based on performance needs for hackathon)
# For webapp speed, we often use exact intersection first constraint.
try:
    # A small, fast model
    model = SentenceTransformer('all-MiniLM-L6-v2') 
except Exception as e:
    model = None
    print(f"SentenceTransformer not loaded: {e}. Falling back to strict matching.")

def compute_skill_gap(resume_data, jd_data):
    """
    Compares extracted resume skills against JD required skills.
    Categorizes skills into Matching, Missing, and Weak.
    
    resume_data format: [{'skill': 'Python', 'experience_level': 'Advanced', 'confidence': 0.85}, ...]
    jd_data format: ['Python', 'SQL', 'AWS', ...]
    """
    resume_skills_dict = {item['skill'].lower(): item for item in resume_data}
    jd_skills = [skill.lower() for skill in jd_data]
    
    matching_skills = []
    missing_skills = []
    weak_skills = []
    
    # 1. Exact Match Phase (Fast & Acccurate for Taxonomy)
    for jd_skill in jd_skills:
        if jd_skill in resume_skills_dict:
            res_skill_data = resume_skills_dict[jd_skill]
            if res_skill_data['experience_level'].lower() == 'beginner':
                # Exact match but candidate is weak
                weak_skills.append({
                    "skill": jd_skill.title(),
                    "reason": "Entry-level experience detected."
                })
            else:
                matching_skills.append(jd_skill.title())
        else:
            # Check Semantic Similarity Phase (Handling variations)
            # E.g., 'ReactJS' vs 'React Framework'
            found_match = False
            
            if model is not None and resume_skills_dict:
                # Encode the missing JD skill
                jd_emb = model.encode(jd_skill)
                # Encode candidate skills
                res_sk = list(resume_skills_dict.keys())
                res_emb = model.encode(res_sk)
                
                # Compute cosines
                cos_scores = util.cos_sim(jd_emb, res_emb)[0]
                best_match_idx = np.argmax(cos_scores)
                
                if cos_scores[best_match_idx] > 0.85: # High threshold for skills
                    matched_skill = res_sk[best_match_idx]
                    res_skill_data = resume_skills_dict[matched_skill]
                    if res_skill_data['experience_level'].lower() == 'beginner':
                        weak_skills.append({
                            "skill": jd_skill.title(),
                            "matched_as": matched_skill.title(),
                            "reason": "Entry-level experience detected."
                        })
                    else:
                        matching_skills.append(jd_skill.title())
                    found_match = True
                    
            if not found_match:
                missing_skills.append(jd_skill.title())
                
    # Calculate additional metrics for a more comprehensive dashboard
    total_jd_skills = len(jd_skills)
    
    # Matches that are at least Intermediate or Senior
    quality_matches = len(matching_skills) 
    
    # Any match at all (including weak ones)
    total_matches = len(matching_skills) + len(weak_skills)
    
    resume_score = round((total_matches / max(total_jd_skills, 1)) * 100, 1)
    match_percentage = round((quality_matches / max(total_jd_skills, 1)) * 100, 1)
    
    return {
        "matching_skills": list(set(matching_skills)),
        "missing_skills": list(set(missing_skills)),
        "weak_skills": weak_skills,
        "match_percentage": match_percentage,
        "resume_score": resume_score,
        "total_required": total_jd_skills
    }

