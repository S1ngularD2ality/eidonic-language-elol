# glyph_586.py — Decrypt Audio Stream
# -----------------------------------------------------------------------------
# ID:            586
# Pack:          Pack 006 (501–600)
# Name:          Decrypt Audio Stream
# Class:         media_stream
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # chunked unseal
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List

def glyph_586(ct_chunks: List[bytes], tags: List[bytes], *, key: bytes, nonce_base: bytes) -> List[bytes]:
    """
    Decrypt Audio Stream — restore audio chunks from sealed form.

    Returns
    -------
    List[bytes]
    """
    out: List[bytes] = []
    for i, ct in enumerate(ct_chunks):
        sealed = {"nonce": nonce_base + i.to_bytes(4, "big"), "ct": ct, "tag": tags[i]}
        out.append(glyph_502(sealed, key=key))  # type: ignore
    return out
