# glyph_409.py — Priority Ladder
# -----------------------------------------------------------------------------
# ID:            409
# Pack:          Pack 005 (401–500)
# Name:          Priority Ladder
# Class:         scaler
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_409(scores: Sequence[float], *, thresholds: Sequence[float]) -> List[int]:
    """
    Priority Ladder — bucketize scores into integer levels 0..N.

    Overview
    --------
    For ascending thresholds ``t0 <= t1 <= ...``, each score gets level = count(score ≥ ti).

    Parameters
    ----------
    scores     : Sequence[float]
    thresholds : Sequence[float]  (ascending)

    Returns
    -------
    List[int] : levels per score.

    Examples
    --------
    >>> glyph_409([0.1, 0.5, 0.9], thresholds=[0.2, 0.8])
    [0, 1, 2]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n·m)
    - Space : O(n)
    """
    th = sorted(float(t) for t in thresholds)
    out: List[int] = []
    for s in scores:
        lvl = 0
        for t in th:
            if float(s) >= t:
                lvl += 1
        out.append(lvl)
    return out
