# glyph_189.py — Mirror Path Projector
# -----------------------------------------------------------------------------
# ID:            189
# Pack:          Pack 002 (101–200)
# Name:          Mirror Path Projector
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

def glyph_189(path: Sequence[Tuple[int, int]]) -> Tuple[List[int], List[int]]:
    """
    Mirror Path Projector — split 2D path into mirrored axes.

    Overview
    --------
    Returns (y_coords, reversed_x_coords) for path-wise mirror diagnostics.

    Parameters
    ----------
    path : Sequence[Tuple[int,int]]

    Returns
    -------
    (List[int], List[int])
        (ys, mirrored_xs)

    Examples
    --------
    >>> glyph_189([(0,0),(1,2),(2,4)])
    ([0, 1, 2], [4, 2, 0])
    """
    ys = [int(y) for y, _ in path]
    xs = [int(x) for _, x in path][::-1]
    return ys, xs
