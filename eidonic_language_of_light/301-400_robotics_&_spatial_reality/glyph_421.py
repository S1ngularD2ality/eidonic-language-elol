# glyph_421.py — Vision-to-Text Scribe
# -----------------------------------------------------------------------------
# ID:            421
# Pack:          Pack 005 (401–500)
# Name:          Vision-to-Text Scribe
# Class:         scribe
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple

def glyph_421(labels: Sequence[Tuple[str, float, float, float, float]]) -> str:
    """
    Vision-to-Text Scribe — compose a caption from detections.

    Overview
    --------
    Accepts (label, y1, x1, y2, x2) tuples with normalized coords. Sorts by row-major
    (top→bottom, then left→right) and emits a compact, human-readable caption.

    Parameters
    ----------
    labels : Sequence[(str, y1, x1, y2, x2)]
        Detection tuples, coords in [0,1].

    Returns
    -------
    str
        Caption such as "3 objects: person near door; chair".

    Examples
    --------
    >>> glyph_421([("person",0.1,0.1,0.5,0.3), ("door",0.1,0.7,0.6,0.9)])
    '2 objects: person near door'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    if not labels:
        return "no objects"
    items = [(str(n), float(y1), float(x1), float(y2), float(x2)) for n,y1,x1,y2,x2 in labels]
    items.sort(key=lambda t: (t[1], t[2]))
    names = [t[0] for t in items]
    if len(names) >= 2:
        caption = f"{names[0]} near {names[1]}"
    else:
        caption = names[0]
    if len(names) > 2:
        caption += "".join(f"; {n}" for n in names[2:])
    return f"{len(names)} objects: {caption}"
