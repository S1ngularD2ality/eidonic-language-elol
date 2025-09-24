# glyph_293.py — Soul Cascade Diverger
# -----------------------------------------------------------------------------
# ID:            293
# Pack:          Pack 003 (201–300)
# Name:          Soul Cascade Diverger
# Class:         transform
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_293(seq: Sequence[float], *, asym: float = 0.3) -> List[float]:
    """
    Soul Cascade Diverger — break symmetry by forward shift mixing.

    Overview
    --------
    y[i]=(1-a)*x[i] + a*x[(i+1) mod n], with a ∈ [0,1].

    Parameters
    ----------
    seq : Sequence[float]
    asym : float, optional (default: 0.3)

    Returns
    -------
    List[float]
        Diverged sequence.

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0: return []
    a = max(0.0, min(1.0, float(asym)))
    return [(1-a)*x[i] + a*x[(i+1) % n] for i in range(n)]
