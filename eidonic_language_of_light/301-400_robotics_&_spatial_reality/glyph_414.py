# glyph_414.py — Keepalive Pact
# -----------------------------------------------------------------------------
# ID:            414
# Pack:          Pack 005 (401–500)
# Name:          Keepalive Pact
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_414(peers: Sequence[str], *, tag: str = "ping") -> List[str]:
    """
    Keepalive Pact — craft minimal keepalive messages for peers.

    Overview
    --------
    Emits strings of the form ``"{tag}@{peer}"`` for each peer.

    Parameters
    ----------
    peers : Sequence[str]
    tag   : str, optional (default: "ping")

    Returns
    -------
    List[str]

    Examples
    --------
    >>> glyph_414(["a","b"], tag="hb")
    ['hb@a', 'hb@b']

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    return [f"{tag}@{p}" for p in peers]
