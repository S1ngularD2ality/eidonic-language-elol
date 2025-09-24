# glyph_137.py — Symbolic Thread Expander
# -----------------------------------------------------------------------------
# ID:            137
# Pack:          Pack 002 (101–200)
# Name:          Symbolic Thread Expander
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, List

def glyph_137(seed: Mapping[str, float], *, repeat: int = 2) -> List[str]:
    """
    Symbolic Thread Expander — n-gram repetition of keys.

    Overview
    --------
    For each key `k`, emit `k*repeat`. Order follows input mapping iteration.

    Parameters
    ----------
    seed : Mapping[str, float]
    repeat : int, optional (default: 2)

    Returns
    -------
    List[str]
        Expanded keys.
    """
    if repeat < 1:
        return []
    return [str(k) * repeat for k in seed.keys()]
