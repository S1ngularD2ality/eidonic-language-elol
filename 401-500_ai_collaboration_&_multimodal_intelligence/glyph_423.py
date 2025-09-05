# glyph_423 – MULTI_AGENT_LOOP
# Create a synchronized, repeating action loop among agents

def glyph_423(agent_list, action, rounds=1):
    """
    agent_list: list of agents
    action: callable
    rounds: how many cycles
    Returns: list of action results
    """
    results = []
    for _ in range(rounds):
        for agent in agent_list:
            results.append((agent, action(agent)))
    return results
