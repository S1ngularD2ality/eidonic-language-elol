# glyph_255.py — Anchor Sequence Fluctuator
# -----------------------------------------------------------------------------
# ID:            255
# Pack:          Pack 003 (201–300)
# Name:          Anchor Sequence Fluctuator
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_255(seq: Sequence[float], *, jitter: float = 0.1) -> List[float]:
    """
    Anchor Sequence Fluctuator — deterministic micro-jitter injection.

    Overview
    --------
    Adds ±jitter alternating by index; stateless and repeatable.

    Parameters
    ----------
    seq : Sequence[float]
    jitter : float, optional (default: 0.1)

    Returns
    -------
    List[float]
        Fluctuated sequence.

    Examples
    --------
    >>> glyph_255([0,0,0,0], jitter=0.5)
    [0.5, -0.5, 0.5, -0.5]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    j = float(jitter)
    return [float(v) + (j if (i % 2 == 0) else -j) for i, v in enumerate(seq)]
