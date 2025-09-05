# glyph_368 – ENVIRONMENTAL_HEALTH
# Aggregate health/safety metrics for real-time environment assessment

def glyph_368(metrics):
    """
    metrics: dict with keys 'air', 'water', 'noise', etc.
    Returns: 'safe' or 'unsafe'
    """
    return "unsafe" if any(v > 0.8 for v in metrics.values()) else "safe"
