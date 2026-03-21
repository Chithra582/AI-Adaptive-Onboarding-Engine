import spacy
import re
from dataset_loader import get_all_skills

# Use small spacy model again
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    nlp = None 

class JDParser:
    def __init__(self):
        self.taxonomy = [skill.lower() for skill in get_all_skills()]

    def extract_skills(self, jd_text):
        """Analyzes Job Description text to extract required skills using precise boundaries."""
        extracted = []
        text_lower = jd_text.lower()
        
        for skill in self.taxonomy:
            pattern = r'\b' + re.escape(skill) + r'(?:\b|$)'
            if '+' in skill or '#' in skill or '.' in skill:
                 pattern = r'(?:\b|\s)' + re.escape(skill) + r'(?:\s|$)'
                 
            if re.search(pattern, text_lower):
                extracted.append(skill.title() if skill.islower() else skill)
                
        return list(set(extracted))

from ai_extractor import extract_skills_with_llm

def parse_jd(jd_text):
    if not jd_text or len(jd_text.strip()) == 0:
        return {"error": "Empty Job Description"}
    
    # AI Powered extraction for better accuracy
    ai_skills = extract_skills_with_llm(jd_text, context="jd")
    
    if ai_skills:
        return {"required_skills": ai_skills}
        
    # Regex Fallback
    parser = JDParser()
    skills = parser.extract_skills(jd_text)
    return {"required_skills": skills}
