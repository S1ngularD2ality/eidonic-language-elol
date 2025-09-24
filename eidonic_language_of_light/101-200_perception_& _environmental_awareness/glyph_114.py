# glyph_114.py — Polarity Shift Equalizer
# -----------------------------------------------------------------------------
# ID:            114
# Pack:          Pack 002 (101–200)
# Name:          Polarity Shift Equalizer
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_114(seq: Sequence[float]) -> Tuple[List[float], float, float]:
    """
    Polarity Shift Equalizer — center positive/negative means to parity.

    Overview
    --------
    Compute means µ+ and µ- over positive/negative subsets; shift positives by -µ+,
    negatives by -µ-. Returns (equalized, µ+, µ-).

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], float, float)
        (equalized, pos_mean, neg_mean)

    Examples
    --------
    >>> glyph_114([-2,-1,0,1,2])[1:]  # means
    (1.5, -1.5)

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    pos = [float(v) for v in seq if v > 0]
    neg = [float(v) for v in seq if v < 0]
    mup = (sum(pos)/len(pos)) if pos else 0.0
    mun = (sum(neg)/len(neg)) if neg else 0.0
    out: List[float] = []
    for v in seq:
        fv = float(v)
        if fv > 0: out.append(fv - mup)
        elif fv < 0: out.append(fv - mun)
        else: out.append(0.0)
    return out, mup, mun
