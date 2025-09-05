# glyph_441 – ROLE_MATRIX
# Create a dynamic role matrix for all agents based on skill and need

def glyph_441(agent_skills, required_roles):
    """
    agent_skills: dict of agent:[skills]
    required_roles: list of roles
    Returns: dict of role:assigned_agent
    """
    assignments = {}
    for role in required_roles:
        for agent, skills in agent_skills.items():
            if role in skills and role not in assignments:
                assignments[role] = agent
                break
    return assignments
