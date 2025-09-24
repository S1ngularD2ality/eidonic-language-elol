# glyph_223.py — Timeline Pulse Reflector
# -----------------------------------------------------------------------------
# ID:            223
# Pack:          Pack 003 (201–300)
# Name:          Timeline Pulse Reflector
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_223(seq: Sequence[float], *, mix: float = 0.5) -> List[float]:
    """
    Timeline Pulse Reflector — mix a sequence with its reverse.

    Overview
    --------
    y[i] = (1-mix)*x[i] + mix*x[n-1-i]; mix∈[0,1].

    Parameters
    ----------
    seq : Sequence[float]
    mix : float, optional (default: 0.5)

    Returns
    -------
    List[float]
        Reflected blend.

    Examples
    --------
    >>> glyph_223([1,2,3,4], mix=1.0)
    [4.0, 3.0, 2.0, 1.0]
    """
    x = [float(v) for v in seq]
    n = len(x)
    m = max(0.0, min(1.0, float(mix)))
    return [(1-m)*x[i] + m*x[n-1-i] for i in range(n)]
