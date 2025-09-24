# glyph_130.py — Phase Memory Equalizer
# -----------------------------------------------------------------------------
# ID:            130
# Pack:          Pack 002 (101–200)
# Name:          Phase Memory Equalizer
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_130(seq: Sequence[float]) -> Tuple[List[float], float, float]:
    """
    Phase Memory Equalizer — standardize to zero mean and unit variance.

    Overview
    --------
    Returns normalized sequence and (mean, std) used.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], float, float)
        (normalized, mean, std)
    """
    n = len(seq)
    if n == 0:
        return [], 0.0, 1.0
    m = sum(float(v) for v in seq)/n
    var = sum((float(v)-m)**2 for v in seq)/n
    s = (var**0.5) or 1.0
    return [(float(v)-m)/s for v in seq], m, s
