# glyph_425.py — Caption Smith
# -----------------------------------------------------------------------------
# ID:            425
# Pack:          Pack 005 (401–500)
# Name:          Caption Smith
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_425(objects: Sequence[str]) -> str:
    """
    Caption Smith — list-style caption from object names.

    Overview
    --------
    Returns "objects: a, b, c" or "no objects" if empty.

    Parameters
    ----------
    objects : Sequence[str]

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_425(["tree","car"])
    'objects: tree, car'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if not objects:
        return "no objects"
    return "objects: " + ", ".join(str(o) for o in objects)
