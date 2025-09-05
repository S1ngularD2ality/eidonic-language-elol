# glyph_476 – STRATEGY_SHIFT
# Shift operational strategy for the entire collective

def glyph_476(collective, new_strategy):
    """
    collective: dict of agent:current_strategy
    new_strategy: string
    Returns: updated strategies
    """
    return {a: new_strategy for a in collective}
