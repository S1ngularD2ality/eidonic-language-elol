# glyph_500 – FINAL_SYNTH
# Synthesize the collective's state into a unified summary

def glyph_500(agent_states):
    """
    agent_states: dict of agent:state
    Returns: unified state summary
    """
    return "; ".join(f"{a}:{s}" for a, s in agent_states.items())
