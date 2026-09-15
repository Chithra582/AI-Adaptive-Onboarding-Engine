# Explainability & Decision-Making Architecture

**Agent**: AI-Adaptive Onboarding Engine  
**Domain**: HR & Recruiting  
**Version**: 1.0.0  
**Specification**: OpenGAP 0.1.0  

---

## 1. How the Agent Decides

The AI-Adaptive Onboarding Engine makes decisions through a transparent, multi-stage deterministic and semantic pipeline rather than an opaque black box:

```
[Resume PDF] --------> [Text Extraction] ---> [Skill Entity Recognition] --+
                                                                          |
                                                                          v
[Job Description] ---> [Text Extraction] ---> [Taxonomy Normalization] -> [Cosine Similarity & Gap Engine]
                                                                          |
                                                                          v
                                              [Roadmap Generator] <-------+ (Matching, Weak, Missing)
                                                      |
                                                      v
                                        [Personalized Learning Path]
```

### Stage 1: Resume & Job Description Parsing
- **PDF Extraction**: Extracts text layers using `PyPDF2` with clean whitespace preservation.
- **Entity Matching**: Uses `spaCy` tokenization combined with regular expression boundary matching (`\b<skill>\b`) against a standardized 150+ technology taxonomy.
- **Experience Level Detection**: Scans a contextual window (-100 to +100 characters around detected skill mentions) searching for seniority indicators (`senior`, `lead`, `architect`, `expert`, `built`, `years`).
  - Score >= 2 seniority signals: **Advanced**
  - Score = 1 action signal: **Intermediate**
  - Default: **Beginner**

### Stage 2: Semantic Skill Gap Analysis
- **Direct Matching**: Compares extracted candidate skills against required JD skills.
- **Semantic Inference**: For skills without exact literal matches, the engine computes cosine similarity over high-dimensional dense vector embeddings (`sentence-transformers/all-MiniLM-L6-v2`):
  $$\text{Similarity}(v_{\text{req}}, v_{\text{cand}}) = \frac{v_{\text{req}} \cdot v_{\text{cand}}}{\|v_{\text{req}}\| \|v_{\text{cand}}\|}$$
  - Similarity $\ge 0.85$: Recognized as a semantic match (e.g., `ReactJS` $\approx$ `React Framework`).
  - Candidate skill experience = `Beginner` but required in JD: Classified as **Weak Skill**.
  - No match found: Classified as **Missing Skill**.

### Stage 3: Dynamic Learning Pathway Generation
- **Upskill Tracks**: Weak skills trigger targeted upskilling modules (2 weeks) focusing on production architectures and best practices.
- **Foundational Tracks**: Missing skills generate binary stepped modules:
  1. *Beginner/Theory* (2 weeks) – Fundamental syntax, mechanics, and starter tutorials.
  2. *Applied/Intermediate* (3 weeks) – Hands-on implementations, real-world patterns, and documentation deep-dives.
- **LLM Enhancement**: When configured with a Hugging Face API key, the engine augments rule steps with customized pedagogical advice generated via `mistralai/Mistral-7B-Instruct-v0.2`.

---

## 2. Data It Uses

The engine draws upon three primary public and standardized corpora:

1. **O*NET (Occupational Information Network) Database**:
   - Source: U.S. Department of Labor (O*NET 28.0+ release).
   - Usage: Standardized skill hierarchy, role ontology, and standardized occupational capability classifications.
2. **Kaggle Resume Dataset**:
   - Source: Sneha Anbhawal Resume Dataset (2,400+ categorized resumes across 24 industry disciplines).
   - Usage: Used to benchmark entity extraction heuristics, section header patterns, and experience descriptor vocabularies.
3. **Kaggle Job Descriptions Dataset**:
   - Source: Kshitiz Regmi Jobs & Job Descriptions Corpus.
   - Usage: Informs frequency weighting of technical requirements across modern engineering and tech roles.
4. **Local Vector Embeddings**:
   - `sentence-transformers/all-MiniLM-L6-v2` (384-dimensional dense vectors fine-tuned for semantic textual similarity).

---

## 3. Limitations

Users, recruiters, and hiring managers should be aware of the following known limitations:

1. **Text-Based Extraction Only**:
   - The engine parses textual data from standard PDF formats. Scanned image resumes without embedded OCR text layers will not yield extractable entities.
2. **Taxonomy Boundary**:
   - Novel, highly proprietary internal corporate tools not present in O*NET or public tech taxonomies will be flagged as unclassified unless mapped in the custom dictionary.
3. **Experience Heuristics**:
   - Experience level is inferred based on linguistic proximity cues (e.g., "5 years", "lead"). Highly non-standard resume formats or unconventional storytelling may affect precision.
4. **Language Support**:
   - Currently optimized for English-language resumes and job descriptions. Multilingual parsing requires additional language models.
5. **No Final Employment Decision**:
   - This tool is an educational onboarding accelerator and gap diagnostic instrument. It is **not** an automated hiring or rejection system.

---

## 4. Ethical Safeguards & Fair Use

- **Zero Demographic Bias**: The skill parser operates exclusively on technical keywords, tools, and experience verbs. It explicitly discards name, gender, race, age, location, and educational institutions during evaluation.
- **Privacy & Data Protection**: All resume parsing occurs in-memory for the duration of the request session. No Personal Identifiable Information (PII) is written to disk or shared with external third parties without user authorization.
