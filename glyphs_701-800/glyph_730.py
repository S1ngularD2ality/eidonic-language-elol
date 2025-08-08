# glyph_730 – SAFETY_HYPOTHESIS_TEST
# One-sided hypothesis test on a safety metric vs threshold.

import statistics
import math

def glyph_730(samples, safe_threshold, alpha=0.05):
    """
    samples: list[float] smaller is safer (e.g., error rate)
    H0: mean >= safe_threshold; H1: mean < safe_threshold
    Returns: {'p_value': float, 'reject_h0': bool}
    """
    if not samples:
        return {"p_value": 1.0, "reject_h0": False}
    m = statistics.mean(samples)
    s = statistics.pstdev(samples) or 1e-9
    z = (safe_threshold - m) / (s / math.sqrt(len(samples)))
    # p-value for normal approx (one-sided)
    from math import erf, sqrt
    p = 0.5 * (1.0 - erf(z / sqrt(2)))
    return {"p_value": p, "reject_h0": p < alpha}
