# glyph_019.py — Light Thread Activator
# -----------------------------------------------------------------------------
# ID:            019
# Pack:          Pack 001 (000–100)
# Name:          Light Thread Activator
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_019(seq: Sequence[float], *, step: int) -> List[float]:
    """
    Light Thread Activator — sample a signal at regular intervals (time dilation).

    Overview
    --------
    Takes every `step`-th element, starting at 0.

    Parameters
    ----------
    seq : Sequence[float]
    step : int
        Sampling stride (>= 1).

    Returns
    -------
    List[float]
        Sampled subsequence.

    Examples
    --------
    >>> glyph_019([0,1,2,3,4,5], step=2)
    [0.0, 2.0, 4.0]
    """
    s = max(1, int(step))
    return [float(seq[i]) for i in range(0, len(seq), s)]
