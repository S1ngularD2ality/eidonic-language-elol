# glyph_501.py — Data Seal
# -----------------------------------------------------------------------------
# ID:            501
# Pack:          Pack 006 (501–600)
# Name:          Data Seal
# Class:         crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # stream-PRF + HMAC using hashlib; no RNG, no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib
from typing import Dict

def glyph_501(plain: bytes, *, key: bytes, nonce: bytes) -> Dict[str, bytes]:
    """
    Data Seal — deterministic authenticated sealing (demo-grade).

    Overview
    --------
    Derives a bytewise keystream via SHA-256(key || nonce || counter) and XORs it
    with `plain` to produce `ct`. Produces integrity tag:
    `tag = SHA256(key || nonce || ct)`. This is **educational**, not production crypto.

    Parameters
    ----------
    plain : bytes
    key   : bytes
    nonce : bytes

    Returns
    -------
    Dict[str, bytes] : {'nonce': bytes, 'ct': bytes, 'tag': bytes}

    Examples
    --------
    >>> p = b'hello'
    >>> sealed = glyph_501(p, key=b'k', nonce=b'n')
    >>> isinstance(sealed['ct'], bytes) and len(sealed['tag']) == 32
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(len(plain))
    - Space : O(1)
    """
    def stream(n: int) -> bytes:
        h = hashlib.sha256(key + nonce + n.to_bytes(8, "big")).digest()
        return h
    out = bytearray()
    i = 0
    while i < len(plain):
        block = stream(i // 32)
        for b in block:
            if i >= len(plain):
                break
            out.append(plain[i] ^ b)
            i += 1
    ct = bytes(out)
    tag = hashlib.sha256(key + nonce + ct).digest()
    return {"nonce": nonce, "ct": ct, "tag": tag}
