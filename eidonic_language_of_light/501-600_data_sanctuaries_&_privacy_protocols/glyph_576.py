# glyph_576.py — Decrypt Log Stream
# -----------------------------------------------------------------------------
# ID:            576
# Pack:          Pack 006 (501–600)
# Name:          Decrypt Log Stream
# Class:         stream_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # chunked unseal; no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List, Mapping

def glyph_576(ct_chunks: List[bytes], tags: List[bytes], *, key: bytes, nonce_base: bytes) -> List[str]:
    """
    Decrypt Log Stream — unseal chunked log lines.

    Returns
    -------
    List[str]

    Examples
    --------
    >>> env = glyph_575(['a','b'], key=b'k', nonce=b'n')
    >>> glyph_576(env['ct_chunks'], env['tags'], key=b'k', nonce_base=env['nonce_base'])
    ['a', 'b']
    """
    out: List[str] = []
    for i, ct in enumerate(ct_chunks):
        sealed = {"nonce": nonce_base + i.to_bytes(4, "big"), "ct": ct, "tag": tags[i]}
        out.append(glyph_502(sealed, key=key).decode("utf-8"))  # type: ignore
    return out
