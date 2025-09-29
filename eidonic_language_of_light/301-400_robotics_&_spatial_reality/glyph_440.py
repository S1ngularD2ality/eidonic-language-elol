# glyph_440.py — Semantic Index
# -----------------------------------------------------------------------------
# ID:            440
# Pack:          Pack 005 (401–500)
# Name:          Semantic Index
# Class:         indexer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Dict, List

def glyph_440(docs: Sequence[str], embeddings: Sequence[Sequence[float]]) -> Dict[str, List[int]]:
    """
    Semantic Index — coarse inverted index over top-1 dimension.

    Overview
    --------
    For each document, find argmax over its embedding and index the doc under that id.

    Parameters
    ----------
    docs       : Sequence[str]
    embeddings : Sequence[Sequence[float]]

    Returns
    -------
    Dict[str, List[int]] : dim_id → list of doc indices.

    Examples
    --------
    >>> glyph_440(["a","b"], [[0.1,0.9],[0.8,0.2]])
    {'1': [0], '0': [1]}

    Exceptions
    ----------
    - ValueError : if lengths differ or any embedding is empty.

    Complexity
    ----------
    - Time  : O(N·D)
    - Space : O(N)
    """
    if len(docs) != len(embeddings):
        raise ValueError("docs and embeddings must have the same length")
    buckets: Dict[str, List[int]] = {}
    for i, vec in enumerate(embeddings):
        if not vec:
            raise ValueError("embedding vectors must be non-empty")
        j = max(range(len(vec)), key=lambda k: float(vec[k]))
        buckets.setdefault(str(j), []).append(i)
    return buckets
