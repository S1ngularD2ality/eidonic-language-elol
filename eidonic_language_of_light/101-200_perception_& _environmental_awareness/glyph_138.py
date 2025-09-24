# glyph_138.py — Thought Signal Reflector
# -----------------------------------------------------------------------------
# ID:            138
# Pack:          Pack 002 (101–200)
# Name:          Thought Signal Reflector
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

def glyph_138(seq: Sequence[float]) -> List[float]:
    """
    Thought Signal Reflector — append the reversed sequence to itself.

    Overview
    --------
    y = x + reverse(x).

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    List[float]
        Reflected series.
    """
    return [float(v) for v in seq] + [float(v) for v in reversed(seq)]
