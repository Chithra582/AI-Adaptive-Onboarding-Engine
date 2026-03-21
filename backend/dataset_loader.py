import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'skills_taxonomy.db')

# Mock data for the hackathon version representing preprocessed Kaggle / O*NET data
MOCK_SKILLS = [
    # Top Programming Languages
    {"name": "Python", "category": "Programming Language", "importance": 95},
    {"name": "JavaScript", "category": "Programming Language", "importance": 90},
    {"name": "Java", "category": "Programming Language", "importance": 85},
    {"name": "C++", "category": "Programming Language", "importance": 80},
    {"name": "C#", "category": "Programming Language", "importance": 80},
    {"name": "Ruby", "category": "Programming Language", "importance": 70},
    {"name": "PHP", "category": "Programming Language", "importance": 75},
    {"name": "Go", "category": "Programming Language", "importance": 85},
    {"name": "Rust", "category": "Programming Language", "importance": 80},
    {"name": "Swift", "category": "Programming Language", "importance": 80},
    {"name": "Kotlin", "category": "Programming Language", "importance": 85},
    {"name": "TypeScript", "category": "Programming Language", "importance": 90},

    # Frontend
    {"name": "React", "category": "Frontend Framework", "importance": 90},
    {"name": "Angular", "category": "Frontend Framework", "importance": 80},
    {"name": "Vue.js", "category": "Frontend Framework", "importance": 80},
    {"name": "HTML", "category": "Web Technology", "importance": 90},
    {"name": "CSS", "category": "Web Technology", "importance": 90},
    {"name": "Tailwind", "category": "Frontend Framework", "importance": 85},
    {"name": "Redux", "category": "State Management", "importance": 80},
    {"name": "Next.js", "category": "Frontend Framework", "importance": 85},

    # Backend
    {"name": "FastAPI", "category": "Backend Framework", "importance": 80},
    {"name": "Node.js", "category": "Backend Framework", "importance": 90},
    {"name": "Express", "category": "Backend Framework", "importance": 85},
    {"name": "Django", "category": "Backend Framework", "importance": 85},
    {"name": "Flask", "category": "Backend Framework", "importance": 80},
    {"name": "Spring Boot", "category": "Backend Framework", "importance": 85},

    # Databases
    {"name": "SQL", "category": "Database", "importance": 90},
    {"name": "PostgreSQL", "category": "Database", "importance": 85},
    {"name": "MySQL", "category": "Database", "importance": 85},
    {"name": "MongoDB", "category": "Database", "importance": 80},
    {"name": "Redis", "category": "Database", "importance": 75},
    {"name": "Elasticsearch", "category": "Database", "importance": 75},

    # DevOps & Cloud
    {"name": "Docker", "category": "DevOps", "importance": 90},
    {"name": "Kubernetes", "category": "DevOps", "importance": 85},
    {"name": "AWS", "category": "Cloud", "importance": 95},
    {"name": "GCP", "category": "Cloud", "importance": 80},
    {"name": "Azure", "category": "Cloud", "importance": 85},
    {"name": "Git", "category": "Version Control", "importance": 95},
    {"name": "CI/CD", "category": "DevOps", "importance": 85},
    {"name": "Jenkins", "category": "DevOps", "importance": 75},
    {"name": "Terraform", "category": "DevOps", "importance": 80},
    {"name": "Linux", "category": "Operating System", "importance": 90},

    # AI / Data Science
    {"name": "Machine Learning", "category": "Data Science", "importance": 90},
    {"name": "Deep Learning", "category": "Data Science", "importance": 85},
    {"name": "Natural Language Processing", "category": "Data Science", "importance": 85},
    {"name": "Computer Vision", "category": "Data Science", "importance": 80},
    {"name": "TensorFlow", "category": "Data Science", "importance": 85},
    {"name": "PyTorch", "category": "Data Science", "importance": 85},
    {"name": "Pandas", "category": "Data Science", "importance": 85},
    {"name": "NumPy", "category": "Data Science", "importance": 85},
    {"name": "Data Analysis", "category": "Data Science", "importance": 80},
    {"name": "Data Engineering", "category": "Data Science", "importance": 85},

    # Architecture & Concepts
    {"name": "Microservices", "category": "Architecture", "importance": 85},
    {"name": "REST API", "category": "Architecture", "importance": 90},
    {"name": "GraphQL", "category": "Architecture", "importance": 80},
    {"name": "Agile", "category": "Methodology", "importance": 85},
    {"name": "Scrum", "category": "Methodology", "importance": 80},
]

def init_db():
    """Initializes a mock SQLite database with preprocessed skill data."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            category TEXT,
            importance INTEGER
        )
    ''')
    
    # Insert mock data directly bypassing the count check, taking advantage of UNIQUE constraints
    for skill in MOCK_SKILLS:
        cursor.execute('''
            INSERT OR IGNORE INTO skills (name, category, importance)
            VALUES (?, ?, ?)
        ''', (skill['name'], skill['category'], skill['importance']))
            
    conn.commit()
    conn.close()

def get_all_skills():
    """Retrieves all recognized skills from the taxonomy."""
    # Ensure DB is initialized
    if not os.path.exists(DB_PATH):
        init_db()
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM skills')
    skills = [row[0] for row in cursor.fetchall()]
    conn.close()
    return skills

# Initialize the mock database upon import
init_db()
