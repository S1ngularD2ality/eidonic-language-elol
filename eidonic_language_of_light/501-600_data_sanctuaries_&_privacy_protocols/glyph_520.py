# glyph_520.py — Encrypt Stream
# -----------------------------------------------------------------------------
# ID:            520
# Pack:          Pack 006 (501–600)
# Name:          Encrypt Stream
# Class:         crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True  # chunked PRF stream
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Dict, List

def glyph_520(chunks: Sequence[bytes], *, key: bytes, nonce: bytes) -> Dict[str, List[bytes]]:
    """
    Encrypt Stream — seal a list of chunks with rolling counter.

    Overview
    --------
    Applies the glyph_501 PRF per-chunk with counter = chunk_index.

    Parameters
    ----------
    chunks : Sequence[bytes]
    key    : bytes
    nonce  : bytes

    Returns
    -------
    Dict[str,List[bytes]] : {'nonce': [nonce], 'ct_chunks': [...], 'tags': [...]}

    Examples
    --------
    >>> out = glyph_520([b'a', b'b'], key=b'k', nonce=b'n')
    >>> len(out['ct_chunks']) == 2 and len(out['tags']) == 2
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(total_bytes)
    - Space : O(total_bytes)
    """
    cts: List[bytes] = []
    tags: List[bytes] = []
    for i, ch in enumerate(chunks):
        sealed = glyph_501(ch, key=key, nonce=nonce + i.to_bytes(4, "big"))  # type: ignore
        cts.append(sealed["ct"]); tags.append(sealed["tag"])
    return {"nonce": [nonce], "ct_chunks": cts, "tags": tags}
