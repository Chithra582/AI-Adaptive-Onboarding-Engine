# Segregation of Duties (SOD)

## Assigned Roles

### Role 1: `onboarding-analyst`
- **Scope**: Parses resumes and job descriptions, normalizes taxonomy names, detects skill entities, and calculates gaps.
- **Restrictions**: Cannot alter curriculum templates or publish final learning assignments.

### Role 2: `roadmap-synthesizer`
- **Scope**: Ingests identified gaps from the analyst role, constructs chronological pathways, maps learning resources, and calls generative LLM endpoints.
- **Restrictions**: Cannot modify raw candidate extraction scores or alter skill matching thresholds.
