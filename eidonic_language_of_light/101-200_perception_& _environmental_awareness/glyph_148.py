# glyph_148.py — Harmonic Flow Interrupter
# -----------------------------------------------------------------------------
# ID:            148
# Pack:          Pack 002 (101–200)
# Name:          Harmonic Flow Interrupter
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_148(x: float, *, lower: float = -1.0, upper: float = 1.0) -> float:
    """
    Harmonic Flow Interrupter — clamp a value into [lower, upper].

    Overview
    --------
    Useful guardrail for feedback or uncontrolled accumulation.

    Parameters
    ----------
    x : float
    lower : float, optional (default: -1.0)
    upper : float, optional (default:  1.0)

    Returns
    -------
    float
        Clamped value.

    Examples
    --------
    >>> glyph_148(5, lower=0, upper=1)
    1.0
    """
    lo = min(lower, upper); hi = max(lower, upper)
    v = float(x)
    return lo if v < lo else (hi if v > hi else v)
