from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import io

# Import our custom modules
from dataset_loader import init_db
from resume_parser import parse_resume
from jd_parser import parse_jd
from skill_gap import compute_skill_gap
from roadmap_generator import generate_roadmap

app = FastAPI(title="AI-Adaptive Onboarding Engine API")

# Enable CORS for React frontend (Vite defaults to port 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Startup event to ensure DB is initialized
@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "AI-Adaptive Onboarding Engine API is running"}

import traceback
from fastapi.responses import JSONResponse

@app.post("/analyze")
async def analyze_full_profile(
    resume: UploadFile = File(..., description="PDF Resume File"),
    jd_text: str = Form(..., description="Job Description Text")
):
    """
    Main endpoint that:
    1. Parses the PDF Resume -> Extracted Skills
    2. Parses the JD Text -> Required Skills
    3. Computes intersection -> Skill Gaps
    4. Generates a personalized roadmap
    """
    try:
        # 1. Parse Resume
        resume_bytes = await resume.read()
        resume_data = parse_resume(resume_bytes)
        res_skills = resume_data.get("extracted_skills", [])
        
        # 2. Parse JD
        jd_data = parse_jd(jd_text)
        req_skills = jd_data.get("required_skills", [])
        
        # 3. Compute Skill Gap
        gap_analysis = compute_skill_gap(res_skills, req_skills)
        
        # 4. Generate Roadmap
        roadmap = generate_roadmap(gap_analysis["missing_skills"], gap_analysis["weak_skills"])
        
        # Assemble comprehensive response
        return {
            "status": "success",
            "resume_analysis": resume_data,
            "job_description_analysis": jd_data,
            "gap_analysis": gap_analysis,
            "roadmap": roadmap
        }
    except Exception as e:
        error_trace = traceback.format_exc()
        print(f"ERROR OCCURRED: {error_trace}")
        return JSONResponse(
            status_code=500,
            content={"detail": f"Backend Error: {str(e)}. Traceback: {error_trace}"}
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

