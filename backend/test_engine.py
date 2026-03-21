import logging
from dataset_loader import get_all_skills
from jd_parser import JDParser
from skill_gap import compute_skill_gap

print("Total Skills in DB:", len(get_all_skills()))

dummy_jd = "Looking for a React developer with Python and AWS experience."
parser = JDParser()
skills = parser.extract_skills(dummy_jd)
print("Skills Extracted from Dummy JD:", skills)

gap = compute_skill_gap([], skills)
print("Computed Gap Missing Skills:", gap['missing_skills'])
