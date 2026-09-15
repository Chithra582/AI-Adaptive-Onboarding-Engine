# Rules & Operational Constraints

1. **Deterministic Skill Evaluation**:
   - Technical skill verification must always be backed by either literal matching or verified cosine vector similarity ($\ge 0.85$).
   - Never invent or hallucinate candidate skills that do not exist in the resume text.

2. **Roadmap Granularity**:
   - Every generated roadmap step must contain:
     - Clear timeline estimate (e.g. 2 weeks, 3 weeks).
     - Explicit step categorization (`Upskill`, `Foundation`, `Application`).
     - Verified reputable learning references (Coursera, Udemy, Official Docs).

3. **Data Privacy**:
   - Resume content must not be written to persistent public logs.
   - PII (names, phone numbers, addresses, emails) must never be extracted or stored.
