# glyph_639.py — HUMAN_ASSIST_BEACON
# -----------------------------------------------------------------------------
# ID:            639
# Pack:          Pack 007 (601–700)
# Name:          HUMAN_ASSIST_BEACON
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib
from typing import List

def glyph_639(length: int, *, key: bytes = b"", label: bytes = b"ELoL-Assist") -> List[int]:
    """
    HUMAN_ASSIST_BEACON — deterministic on/off pattern for visual beaconing.

    Overview
    --------
    Generates a reproducible 0/1 sequence from a keyed hash stream (opaque; no I/O).

    Parameters
    ----------
    length : int
        Number of elements in the pattern (>= 0).
    key    : bytes, optional
    label  : bytes, optional

    Returns
    -------
    List[int]
        0/1 pattern of requested length.

    Examples
    --------
    >>> p = glyph_639(8, key=b'k'); len(p) == 8 and set(p) <= {0,1}
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    n = max(0, int(length))
    out: List[int] = []
    i = 0
    while len(out) < n:
        block = hashlib.sha256(label + key + i.to_bytes(4, "big")).digest()
        for b in block:
            if len(out) >= n:
                break
            out.append((b >> 7) & 1)  # MSB bit
        i += 1
    return out
