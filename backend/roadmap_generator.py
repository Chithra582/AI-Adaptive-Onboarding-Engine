import os
import requests

import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

def generate_roadmap(missing_skills, weak_skills):
    """
    Generates an adaptive learning roadmap using HuggingFace Inference API if available,
    otherwise gracefully falls back to our robust rule-based engine.
    """
    
    roadmap = []
    step_counter = 1
    
    # Optional Hugging Face Integration (Mistral-7B)
    if HF_API_KEY and len(missing_skills) > 0:
        try:
            headers = {"Authorization": f"Bearer {HF_API_KEY}"}
            API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
            
            prompt = f"[INST] You are an expert AI Career Coach. A candidate is missing the following skills: {', '.join(missing_skills)}. Provide exactly one short, actionable learning step for EACH skill. [/INST]"
            
            response = requests.post(API_URL, headers=headers, json={"inputs": prompt, "parameters": {"max_new_tokens": 150}})
            if response.status_code == 200:
                ai_text = response.json()[0]['generated_text'].replace(prompt, '').strip()
                # If the API succeeds, we append the raw AI advice as a master step
                roadmap.append({
                    "step": step_counter,
                    "skill": "AI Roadmap Synthesis",
                    "type": "AI Generated Path",
                    "title": "Hugging Face Personalized Guide",
                    "description": ai_text,
                    "estimated_time": "Varies",
                    "resources": ["Generated via Mistral-7B"]
                })
                step_counter += 1
                return roadmap # Return early if HF succeeded
        except Exception as e:
            print(f"HF API Failed, falling back to Rules Engine: {e}")

    # --- FALLBACK: Ultra-fast Local Rules Engine ---
    for weak in weak_skills:
        skill = weak['skill']
        roadmap.append({
            "step": step_counter,
            "skill": skill,
            "type": "Upskill",
            "title": f"Advanced {skill} Mastery",
            "description": f"Targeted improvement on {skill} to bridge the gap from beginner to production-level proficiency.",
            "estimated_time": "2 weeks",
            "resources": [
                f"Coursera: Advanced {skill} Patterns",
                f"{skill} Official Documentation Deep Dive",
                f"YouTube: Real-world {skill} Projects"
            ]
        })
        step_counter += 1
        
    for missing in missing_skills:
        roadmap.append({
            "step": step_counter,
            "skill": missing,
            "type": "Foundation",
            "title": f"{missing} Foundations (Beginner)",
            "description": f"Learn the core concepts, syntax, and basic usage of {missing}.",
            "estimated_time": "2 weeks",
            "resources": [
                f"Udemy: {missing} Bootcamp for Beginners",
                f"FreeCodeCamp: {missing} Crash Course"
            ]
        })
        step_counter += 1
        
        roadmap.append({
            "step": step_counter,
            "skill": missing,
            "type": "Application",
            "title": f"Applied {missing} (Intermediate)",
            "description": f"Build practical projects and understand intermediate architectural concepts in {missing}.",
            "estimated_time": "3 weeks",
            "resources": [
                f"Pluralsight: Developing with {missing}",
                f"GitHub: {missing} open source contributions"
            ]
        })
        step_counter += 1
        
    return roadmap

