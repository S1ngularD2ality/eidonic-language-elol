# glyph_275.py — Mirror Stream Defragmenter
# -----------------------------------------------------------------------------
# ID:            275
# Pack:          Pack 003 (201–300)
# Original Name: Mirror Stream Defragmenter
# Manifest Name: Mirror Stream Defragmenter
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
def glyph_275(seq: list[int]) -> list[list[int]]:
    """
    Mirror Stream Defragmenter — group consecutive runs.

    Overview
    --------
    Returns list of contiguous segments with equal values.

    Parameters
    ----------
    seq : list[int]

    Returns
    -------
    list[list[int]]
        Defragmented runs.

    Examples
    --------
    >>> glyph_275([1,1,2,2,2,3])
    [[1, 1], [2, 2, 2], [3]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if not seq: 
        return []
    out = [[seq[0]]]
    for v in seq[1:]:
        if v == out[-1][-1]:
            out[-1].append(v)
        else:
            out.append([v])
    return out
