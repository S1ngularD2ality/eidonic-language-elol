# glyph_747 – DECISION_REHEARSAL
# Simulate decisions before executing them in the live system.

def glyph_747(decision_fn, scenarios):
    """
    decision_fn: callable(scenario) -> result
    scenarios: list of scenario inputs
    Returns: list of (scenario, result)
    """
    return [(s, decision_fn(s)) for s in scenarios]
