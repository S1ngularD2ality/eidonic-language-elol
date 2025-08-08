# glyph_749 – ALIGNMENT_DRIFT_ALERT
# Alert if alignment check pass rate drops below threshold.

def glyph_749(history, threshold=0.95):
    """
    history: list of bool (alignment checks)
    Returns: bool (alert)
    """
    if not history:
        return False
    rate = sum(history)/len(history)
    return rate < threshold
