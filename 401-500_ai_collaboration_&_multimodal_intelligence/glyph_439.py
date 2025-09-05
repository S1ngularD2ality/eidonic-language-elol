# glyph_439 – INTERFACE_CAST
# Instantly create a new interface or dashboard for collective control

def glyph_439(interface_type, agents):
    """
    interface_type: 'dashboard', 'voice', etc.
    agents: list of agents
    Returns: string representation
    """
    return f"{interface_type.capitalize()} for agents: {', '.join(map(str, agents))}"
