# glyph_072.py — Subconscious Frame Realigner
# -----------------------------------------------------------------------------
# ID:            072
# Pack:          Pack 001 (000–100)
# Name:          Subconscious Frame Realigner
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_072(seq: Sequence[float], *, target_mean: float = 0.0, target_std: float = 1.0) -> List[float]:
    """
    Subconscious Frame Realigner — normalize to target mean and std.

    Overview
    --------
    Affine normalization y = (x - mean)/std * target_std + target_mean.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.
    target_mean : float, optional (default: 0.0)
    target_std : float, optional (default: 1.0)

    Returns
    -------
    List[float]
        Normalized sequence.

    Examples
    --------
    >>> glyph_072([1,2,3], target_mean=0, target_std=1)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    n = len(seq)
    if n == 0:
        return []
    m = sum(float(v) for v in seq)/n
    var = sum((float(v)-m)**2 for v in seq)/n
    s = (var**0.5) or 1.0
    tstd = abs(float(target_std)) or 1.0
    return [((float(v)-m)/s)*tstd + float(target_mean) for v in seq]
