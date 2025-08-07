# glyph_429 – CONFLICT_RESOLVE
# Resolve disagreements or conflicting goals among agents

def glyph_429(conflicts):
    """
    conflicts: list of (agent, issue)
    Returns: list of resolved issues
    """
    return [(agent, f"resolved {issue}") for agent, issue in conflicts]
