# glyph_502.py — Data Unseal
# -----------------------------------------------------------------------------
# ID:            502
# Pack:          Pack 006 (501–600)
# Name:          Data Unseal
# Class:         crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib

def glyph_502(sealed: dict, *, key: bytes) -> bytes:
    """
    Data Unseal — verify tag then decrypt with the same PRF stream.

    Overview
    --------
    Validates `SHA256(key || nonce || ct) == tag`; on success, XOR-decrypts.

    Parameters
    ----------
    sealed : {'nonce': bytes, 'ct': bytes, 'tag': bytes}
    key    : bytes

    Returns
    -------
    bytes : plaintext

    Examples
    --------
    >>> s = glyph_501(b'hi', key=b'k', nonce=b'n')
    >>> glyph_502(s, key=b'k')
    b'hi'

    Exceptions
    ----------
    - ValueError : if tag mismatch.

    Complexity
    ----------
    - Time  : O(len(ct))
    - Space : O(1)
    """
    nonce = sealed["nonce"]; ct = sealed["ct"]; tag = sealed["tag"]
    if hashlib.sha256(key + nonce + ct).digest() != tag:
        raise ValueError("authentication failed")
    # same stream as glyph_501
    def stream(n: int) -> bytes:
        return hashlib.sha256(key + nonce + n.to_bytes(8, "big")).digest()
    out = bytearray()
    i = 0
    while i < len(ct):
        block = stream(i // 32)
        for b in block:
            if i >= len(ct):
                break
            out.append(ct[i] ^ b)
            i += 1
    return bytes(out)
