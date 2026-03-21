import spacy
from PyPDF2 import PdfReader
import io
import re
from dataset_loader import get_all_skills

# Load spaCy NLP model (we will use the small english model for the hackathon)
# Note: In a real environment, you'd run `python -m spacy download en_core_web_sm`
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Fallback/mock if spacy model is not downloaded yet (for robust error handling)
    nlp = None 
    print("Warning: en_core_web_sm not found. Falling back to simple string matching.")

class ResumeParser:
    def __init__(self):
        self.taxonomy = [skill.lower() for skill in get_all_skills()]

    def extract_text_from_pdf(self, file_bytes):
        """Extracts plain text from a PDF file."""
        reader = PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
        return text

    def extract_skills(self, text):
        """Extract skills from text by regex matching against our taxonomy."""
        extracted = []
        text_lower = text.lower()
        
        for skill in self.taxonomy:
            # Use regex word boundaries to prevent matching 'C' inside 'React' or 'CSS' inside 'Access'
            # Also handle characters like C++ or C# safely
            pattern = r'\b' + re.escape(skill) + r'(?:\b|$)'
            # Special case for languages with symbols like C++ or C# where \b doesn't work standardly at the end
            if '+' in skill or '#' in skill or '.' in skill:
                 pattern = r'(?:\b|\s)' + re.escape(skill) + r'(?:\s|$)'
                 
            if re.search(pattern, text_lower):
                # Basic mock logic for experience level based on simple keyword context
                experience = "Beginner"
                
                # Check 100 characters around the skill for context clues
                context_match = re.search(r'(.{0,100})' + pattern + r'(.{0,100})', text_lower)
                if context_match:
                    context = context_match.group(1) + context_match.group(2)
                    if any(kw in context for kw in ["senior", "lead", "expert", "years", "architect", "advanced"]):
                        experience = "Advanced"
                    elif any(kw in context for kw in ["developed", "built", "managed", "intermediate", "production"]):
                        experience = "Intermediate"
                    
                extracted.append({
                    "skill": skill.title() if skill.islower() else skill,
                    "experience_level": experience,
                    "confidence": 0.85 
                })
                
        # Return unique skills
        unique_skills = []
        seen = set()
        for s in extracted:
            if s['skill'].lower() not in seen:
                unique_skills.append(s)
                seen.add(s['skill'].lower())
                
        return unique_skills

from ai_extractor import extract_skills_with_llm

def parse_resume(file_bytes):
    parser = ResumeParser()
    text = parser.extract_text_from_pdf(file_bytes)
    
    # Try AI extraction first for better context
    ai_skills = extract_skills_with_llm(text, context="resume")
    
    if ai_skills:
        # Map AI skills format to internal format
        processed_skills = []
        for s in ai_skills:
            processed_skills.append({
                "skill": s.get("skill", "Unknown"),
                "experience_level": s.get("level", "Intermediate"),
                "confidence": 0.95
            })
        return {"extracted_skills": processed_skills, "raw_text_length": len(text)}

    # Fallback to legacy regex parser
    skills = parser.extract_skills(text)
    return {"extracted_skills": skills, "raw_text_length": len(text)}
