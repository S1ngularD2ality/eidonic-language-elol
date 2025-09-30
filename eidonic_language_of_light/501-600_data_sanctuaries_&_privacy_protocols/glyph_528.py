# glyph_528.py — Secure Random
# -----------------------------------------------------------------------------
# ID:            528
# Pack:          Pack 006 (501–600)
# Name:          Secure Random
# Class:         prf_stream
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # PRF stream; no OS RNG
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib

def glyph_528(n: int, *, key: bytes, nonce: bytes) -> bytes:
    """
    Secure Random — SHA-256(key||nonce||counter) stream generator.

    Overview
    --------
    Produces `n` bytes deterministically from (key, nonce).

    Parameters
    ----------
    n     : int
    key   : bytes
    nonce : bytes

    Returns
    -------
    bytes

    Examples
    --------
    >>> len(glyph_528(5, key=b'k', nonce=b'n'))
    5

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    out = bytearray()
    i = 0
    while len(out) < n:
        block = hashlib.sha256(key + nonce + i.to_bytes(8, "big")).digest()
        need = n - len(out)
        out.extend(block[:need])
        i += 1
    return bytes(out)
