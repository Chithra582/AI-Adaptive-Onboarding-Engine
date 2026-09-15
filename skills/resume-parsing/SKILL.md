---
name: resume-parsing
description: Extracts candidate technical skills and experience levels from resumes using NLP and pattern matching.
---

# Resume Parsing Skill

## Overview
This skill extracts plain text from uploaded PDF resumes and executes taxonomy-constrained named entity extraction to identify candidate technical competencies and infer proficiency levels.

## Implementation
- **Text Layer**: PyPDF2 extraction
- **Entity Matching**: Regex word-boundary scanning against standard O*NET tech ontology
- **Experience Context**: Linguistic proximity analysis for seniority cues
