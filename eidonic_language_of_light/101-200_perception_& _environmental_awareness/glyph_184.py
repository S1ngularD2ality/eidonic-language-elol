# glyph_184.py — Harmonic Bridge Constrictor
# -----------------------------------------------------------------------------
# ID:            184
# Pack:          Pack 002 (101–200)
# Name:          Harmonic Bridge Constrictor
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_184(a: Sequence[float], b: Sequence[float], *, mix: float = 0.5) -> List[float]:
    """
    Harmonic Bridge Constrictor — contract two streams toward each other.

    Overview
    --------
    Returns y[i] = (1-mix)*a[i] + mix*b[i] for i up to min(len(a),len(b)).

    Parameters
    ----------
    a, b : Sequence[float]
    mix  : float, optional (default: 0.5)

    Returns
    -------
    List[float]
        Constricted bridge.

    Examples
    --------
    >>> glyph_184([0,0,0], [2,2,2], mix=0.25)
    [0.5, 0.5, 0.5]
    """
    m = min(len(a), len(b))
    r = max(0.0, min(1.0, float(mix)))
    return [(1-r)*float(a[i]) + r*float(b[i]) for i in range(m)]
