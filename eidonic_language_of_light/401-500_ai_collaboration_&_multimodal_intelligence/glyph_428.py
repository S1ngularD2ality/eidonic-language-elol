# glyph_428.py — Grounding Anchor
# -----------------------------------------------------------------------------
# ID:            428
# Pack:          Pack 005 (401–500)
# Name:          Grounding Anchor
# Class:         aligner
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_428(tokens: Sequence[str], classes: Sequence[str]) -> List[int]:
    """
    Grounding Anchor — align tokens to class labels.

    Overview
    --------
    First class whose lowercase contains the token (or vice versa) is chosen.

    Parameters
    ----------
    tokens  : Sequence[str]
    classes : Sequence[str]

    Returns
    -------
    List[int] : per-token class index or -1.

    Examples
    --------
    >>> glyph_428(["red","car"], ["car.1","tree"])
    [0, 0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(T·C)
    - Space : O(1)
    """
    cls = [c.lower() for c in classes]
    out: List[int] = []
    for t in tokens:
        lt = t.lower()
        idx = next((i for i,c in enumerate(cls) if lt in c or c in lt), -1)
        out.append(idx)
    return out
