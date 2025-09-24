# glyph_147.py — Soul Cascade Splitter
# -----------------------------------------------------------------------------
# ID:            147
# Pack:          Pack 002 (101–200)
# Name:          Soul Cascade Splitter
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_147(seq: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Soul Cascade Splitter — decompose into monotone rises and falls.

    Overview
    --------
    Splits the series into two streams: upward deltas (≥0) and downward deltas (≤0)
    accumulated cumulatively.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], List[float])
        (ups, downs) cumulative components.
    """
    if not seq: return [], []
    ups=[0.0]; downs=[0.0]
    for i in range(1, len(seq)):
        d = float(seq[i]) - float(seq[i-1])
        ups.append(ups[-1] + max(d, 0.0))
        downs.append(downs[-1] + min(d, 0.0))
    return ups, downs
