# glyph_466 – ECHO_CHAIN
# Relay a message repeatedly through a defined agent order

def glyph_466(agent_list, message, repeats=1):
    """
    agent_list: list of agents
    message: string
    repeats: number of times to pass through the chain
    Returns: list of (agent, message) in order
    """
    chain = []
    for _ in range(repeats):
        for a in agent_list:
            chain.append((a, message))
    return chain
