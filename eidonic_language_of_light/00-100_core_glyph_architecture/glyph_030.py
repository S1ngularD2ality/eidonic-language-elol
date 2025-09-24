# glyph_030.py — Flow Anchor Sequencer
# -----------------------------------------------------------------------------
# ID:            030
# Pack:          Pack 001 (000–100)
# Name:          Flow Anchor Sequencer
# Class:         control
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_030(seq: Sequence[int], *, start: int = 0, step: int = 1) -> List[int]:
    """
    Flow Anchor Sequencer — generate an arithmetic index aligned to a base sequence.

    Overview
    --------
    Returns indices: start, start+step, ... of same length as `seq`.

    Parameters
    ----------
    seq : Sequence[int]
    start : int, optional (default: 0)
    step : int, optional (default: 1)

    Returns
    -------
    List[int]
        Anchor sequence.

    Examples
    --------
    >>> glyph_030([0,0,0], start=2, step=3)
    [2, 5, 8]
    """
    n = len(seq)
    return [start + i*step for i in range(n)]
