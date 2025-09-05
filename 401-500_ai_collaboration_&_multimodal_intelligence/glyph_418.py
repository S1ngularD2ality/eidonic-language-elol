# glyph_418 – TASK_DELEGATE
# Delegate tasks to agents based on skill or availability

def glyph_418(agent_skills, task):
    """
    agent_skills: dict of agent:[skills]
    task: string
    Returns: best agent or None
    """
    for agent, skills in agent_skills.items():
        if task in skills:
            return agent
    return None
