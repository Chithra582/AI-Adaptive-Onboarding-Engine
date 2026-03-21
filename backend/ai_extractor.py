import requests
import json
import re

import os
from dotenv import load_dotenv

load_dotenv()

# Load from environment variable for security
HF_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

def extract_skills_with_llm(text, context="resume"):
    """
    Uses Mistral-7B to extract a clean list of skills from a resume or JD.
    """
    if not HF_API_KEY:
        return []

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    
    if context == "resume":
        prompt = f"[INST] Extract all technical skills and their proficiency (Beginner, Intermediate, Advanced) from this resume. Output ONLY a JSON list of objects like {{\"skill\": \"Python\", \"level\": \"Advanced\"}}. Resume text: {text[:2000]} [/INST]"
    else:
        prompt = f"[INST] Extract all required technical skills from this job description. Output ONLY a comma-separated list of skill names. JD text: {text[:2000]} [/INST]"

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt, "parameters": {"max_new_tokens": 300}})
        if response.status_code == 200:
            ai_text = response.json()[0]['generated_text'].replace(prompt, '').strip()
            
            # Simple JSON extraction from response
            if context == "resume":
                # Look for JSON array pattern
                match = re.search(r'\[.*\]', ai_text, re.DOTALL)
                if match:
                    return json.loads(match.group(0))
            else:
                # Comma separated list
                skills = [s.strip() for s in ai_text.split(',')]
                return [s for s in skills if len(s) > 0]
    except Exception as e:
        print(f"AI Skill Extraction Failed: {e}")
    
    return []
