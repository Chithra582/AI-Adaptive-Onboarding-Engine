"""
CrewAI Export Adapter for OpenGAP Checkpoint 3
"""
from crewai import Agent, Task, Crew

def get_onboarding_crew():
    analyst = Agent(
        role="AI Onboarding & Skill Gap Specialist",
        goal="Extract skills from candidate resumes and map them against job descriptions",
        backstory="Senior technical talent evaluator specializing in O*NET capability mapping.",
        verbose=True
    )

    synthesizer = Agent(
        role="Personalized Learning Path Architect",
        goal="Generate personalized adaptive training pathways to close identified skill gaps",
        backstory="Enterprise learning strategist skilled in building milestone-based developer curriculums.",
        verbose=True
    )

    return Crew(
        agents=[analyst, synthesizer],
        tasks=[]
    )
