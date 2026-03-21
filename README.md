# AI-Adaptive Onboarding Engine 🚀

The **AI-Adaptive Onboarding Engine** is a full-stack, AI-driven platform designed to bridge the gap between candidate expertise and job requirements. By leveraging state-of-the-art LLMs (Mistral-7B) and public datasets (Kaggle/O*NET), it provides automated skill gap analysis and dynamically generates personalized learning roadmaps.

## 🌟 Key Features
- **AI-Powered Skill Extraction**: Uses `Mistral-7B-Instruct-v0.2` via Hugging Face to intelligently parse Resumes and JDs—far surpassing traditional regex or keyword matching.
- **Dynamic Skill Gap Dashboard**: A premium, glassmorphism-style UI that visualizes **Ready Match (%)**, **Resume Strength**, and **Calculated Skill Gaps** at a glance.
- **Personalized Learning Roadmaps**: Automatically generates a step-by-step upskilling path with estimated timelines and curated resources (Coursera, Udemy, etc.).
- **Kaggle & O*NET Integration**: Built on an optimized SQLite taxonomy derived from over 10,000+ job descriptions and industry-standard skill frameworks.

## 🛠️ Tech Stack
- **Frontend**: React (Vite), Tailwind CSS v4, Framer Motion (for animations).
- **Backend**: FastAPI (Python), spaCy, Sentence-Transformers.
- **AI Models**: Mistral-7B (Inference API), all-MiniLM-L6-v2 (Embedding).
- **Database**: SQLite with preprocessed taxonomy for high-performance matching.

## 📂 Project Structure
- `/backend`: Python FastAPI service for AI analysis and roadmap generation.
- `/frontend`: Responsive React web app with modern UI/UX design.
- `/backend/data`: Optimized skill taxonomy and sample test datasets.

## 🚀 Getting Started

### 1. Backend Setup
```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# Install deps
pip install -r requirements.txt
# Start server
uvicorn main:app --reload
```
*Backend runs on `http://127.0.0.1:8000`*

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
*Frontend runs on `http://localhost:5173`*

## 📊 Dataset Attribution
- **Kaggle Resume Dataset**: [snehaanbhawal/resume-dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)
- **Kaggle Jobs Dataset**: [kshitizregmi/jobs-and-job-description](https://www.kaggle.com/datasets/kshitizregmi/jobs-and-job-description)
- **O*NET Content Model**: Standardized occupational skills framework.

## 🏆 Hackathon Submission Details
- **AI/ML Use Case**: Hybrid approach combining semantic embeddings with LLM-based entity extraction.
- **Data Pipeline**: Custom preprocessing script (`preprocess_datasets.py`) to optimize high-volume CSV data for real-time web use.
- **Scalability**: Clean modular architecture ready for production deployment.

---
Built with ❤️ for the Hackathon by the AI-Onboarding Team.
