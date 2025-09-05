# glyph_729 – SHADOW_DECIDER
# Compare shadow model outputs to prod; choose safer/stronger result.

def glyph_729(prod_out, shadow_out, preference="accuracy"):
    """
    prod_out/shadow_out: dict with keys {'score','risk'} (higher score better, lower risk safer)
    preference: 'accuracy' or 'safety'
    Returns chosen label: 'prod' or 'shadow'
    """
    if preference == "safety":
        return "shadow" if shadow_out["risk"] < prod_out["risk"] else "prod"
    return "shadow" if shadow_out["score"] > prod_out["score"] else "prod"
