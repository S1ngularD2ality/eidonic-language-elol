# glyph_707 – TRANSPARENT_REASON_REPORT
# Convert internal reasoning steps to a clean, human-readable report.

def glyph_707(steps):
    """
    steps: list of dicts like {"id": 's1', "claim": '...', "supports": ['s0']}
    Returns: markdown string
    """
    lines = ["# Reasoning Report", ""]
    for s in steps:
        sup = ", ".join(s.get("supports", [])) or "none"
        lines.append(f"- **{s['id']}**: {s['claim']}  (supports: {sup})")
    return "\n".join(lines)
