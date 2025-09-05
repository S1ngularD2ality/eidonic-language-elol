# glyph_828 – HARMONIC_MEAN_FIELD
# Compute harmonic mean over sliding windows; robust to large outliers.

def glyph_828(values, window=5):
    """
    values: list[float] (all > 0 recommended)
    window: sliding window size >=1
    Returns list of harmonic means aligned to centers (edge-clamped).
    """
    if not values:
        return []
    n = len(values)
    out = []
    r = max(0, (window - 1) // 2)
    for i in range(n):
        lo = max(0, i - r)
        hi = min(n, i + r + 1)
        seg = values[lo:hi]
        s = sum(1.0 / max(1e-12, v) for v in seg)
        out.append(len(seg) / s if s else 0.0)
    return out
