# glyph_185.py — Subconscious Field Tuner
# -----------------------------------------------------------------------------
# ID:            185
# Pack:          Pack 002 (101–200)
# Name:          Subconscious Field Tuner
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_185(seq: Sequence[float], *, target_mean: float = 0.0, target_std: float = 1.0) -> Tuple[List[float], float, float]:
    """
    Subconscious Field Tuner — match mean and variance to targets.

    Overview
    --------
    Standardizes x to zero-mean/unit-std, then scales to (target_mean, target_std).

    Parameters
    ----------
    seq : Sequence[float]
    target_mean : float, optional (default: 0.0)
    target_std  : float, optional (default: 1.0)

    Returns
    -------
    (List[float], float, float)
        (tuned_sequence, original_mean, original_std)

    Examples
    --------
    >>> y, m, s = glyph_185([1,2,3], target_mean=10, target_std=2)
    >>> round(sum(y)/len(y), 6)
    10.0
    """
    n = len(seq)
    if n == 0:
        return [], 0.0, 1.0
    m = sum(float(v) for v in seq)/n
    var = sum((float(v)-m)**2 for v in seq)/n
    s = (var**0.5) or 1.0
    tm, ts = float(target_mean), float(target_std) if target_std != 0 else 1.0
    return [tm + ts*((float(v)-m)/s) for v in seq], m, s
