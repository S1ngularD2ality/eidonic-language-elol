# glyph_483.py — Fork Healer
# -----------------------------------------------------------------------------
# ID:            483
# Pack:          Pack 005 (401–500)
# Name:          Fork Healer
# Class:         reconciler
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping, Any, Dict

def glyph_483(chains: Sequence[Sequence[Mapping[str, Any]]]) -> Dict[str, Any]:
    """
    Fork Healer — pick the longest valid chain (by length), prefer lowest checksum.

    Overview
    --------
    Given multiple chains (lists of blocks with 'id' optional), returns summary:
    {'chain_index': i, 'length': L, 'checksum': hex}.

    Parameters
    ----------
    chains : Sequence[Sequence[Mapping[str,Any]]]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_483([[{'id':1}], [{'id':1},{'id':2}]])['length']
    2

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(sum lengths)
    - Space : O(1)
    """
    import hashlib, json
    best = None
    out = {"chain_index": -1, "length": 0, "checksum": ""}
    for i, chain in enumerate(chains):
        L = len(chain)
        digest = hashlib.sha256(json.dumps(chain, sort_keys=True, default=str).encode()).hexdigest()
        key = (-L, digest)  # longest, then lexicographically smaller digest
        if best is None or key < best:
            best = key
            out = {"chain_index": i, "length": L, "checksum": digest}
    return out
