# glyph_124.py — Harmonic Drift Suppressor
# -----------------------------------------------------------------------------
# ID:            124
# Pack:          Pack 002 (101–200)
# Name:          Harmonic Drift Suppressor
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_124(seq: Sequence[float], *, cutoff: float = 0.1) -> List[float]:
    """
    Harmonic Drift Suppressor — high-pass via adjacent differences.

    Overview
    --------
    Compute d[i] = x[i] - x[i-1]; then suppress small |d[i]| < cutoff to 0; 
    reconstruct via cumulative sum.

    Parameters
    ----------
    seq : Sequence[float]
    cutoff : float, optional (default: 0.1)

    Returns
    -------
    List[float]
        Drift-suppressed sequence.

    Examples
    --------
    >>> glyph_124([0,0.1,0.2,0.21,0.22], cutoff=0.15)
    [0.0, 0.0, 0.0, 0.0, 0.0]
    """
    if not seq:
        return []
    diffs = [0.0]
    for i in range(1, len(seq)):
        d = float(seq[i]) - float(seq[i-1])
        diffs.append(d if abs(d) >= cutoff else 0.0)
    out = [float(seq[0])]
    for i in range(1, len(seq)):
        out.append(out[-1] + diffs[i])
    return out
