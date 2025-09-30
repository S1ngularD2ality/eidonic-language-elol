# glyph_479.py — Accord Proof
# -----------------------------------------------------------------------------
# ID:            479
# Pack:          Pack 005 (401–500)
# Name:          Accord Proof
# Class:         verifier
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_479(signatures: Sequence[str], *, quorum: int) -> bool:
    """
    Accord Proof — quorum-based validity of signatures.

    Overview
    --------
    Returns True if count of distinct non-empty signatures >= quorum.

    Parameters
    ----------
    signatures : Sequence[str]
    quorum     : int

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_479(["a","b","a"], quorum=2)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    uniq = {s for s in signatures if s}
    return len(uniq) >= int(quorum)
