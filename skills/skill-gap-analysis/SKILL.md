---
name: skill-gap-analysis
description: Computes literal and semantic similarity between candidate skills and job requirements.
---

# Skill Gap Analysis Skill

## Overview
Evaluates the intersection between extracted candidate skills and role demands, calculating readiness percentage and categorizing competencies into matching, weak, and missing.

## Implementation
- **Exact & Substring Matching**: Fast deterministic matching
- **Semantic Embeddings**: `sentence-transformers/all-MiniLM-L6-v2` dense vector cosine similarity (threshold >= 0.85)
