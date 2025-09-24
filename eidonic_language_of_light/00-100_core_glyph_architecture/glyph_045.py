# glyph_045.py — Mirror Index Translator
# -----------------------------------------------------------------------------
# ID:            045
# Pack:          Pack 001 (000–100)
# Name:          Mirror Index Translator
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_045(seq: Sequence[float]) -> List[float]:
    """
    Mirror Index Translator — reverse a sequence (mirror over its center).

    Overview
    --------
    Produces `seq[::-1]` as floats; useful as a primitive for symmetric blends
    and palindromic patterning.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.

    Returns
    -------
    List[float]
        Reversed sequence.

    Examples
    --------
    >>> glyph_045([1,2,3])
    [3.0, 2.0, 1.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    return [float(v) for v in reversed(seq)]
