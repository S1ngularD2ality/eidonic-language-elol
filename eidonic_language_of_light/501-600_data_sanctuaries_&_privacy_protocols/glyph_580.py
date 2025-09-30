# glyph_580.py — Secure Key Share
# -----------------------------------------------------------------------------
# ID:            580
# Pack:          Pack 006 (501–600)
# Name:          Secure Key Share
# Class:         key_management
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # 2-of-2 XOR split; no RNG
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib
from typing import Tuple

def glyph_580(secret: bytes, *, label: bytes = b"ELoL-KeyShare", key: bytes = b"") -> Tuple[bytes, bytes]:
    """
    Secure Key Share — deterministic 2-of-2 XOR split of a secret.

    Overview
    --------
    Derive a mask via SHA-256(label||key||len||secret) repeated to length; output
    (share_a = mask, share_b = secret XOR mask). Recombine by XORing the two shares.

    Parameters
    ----------
    secret : bytes
    label  : bytes, optional
    key    : bytes, optional

    Returns
    -------
    (bytes, bytes) : (share_a, share_b)

    Examples
    --------
    >>> a,b = glyph_580(b'secret', key=b'k'); bytes(x^y for x,y in zip(a,b)) == b'secret'
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    mask = bytearray()
    i = 0
    while len(mask) < len(secret):
        block = hashlib.sha256(label + key + len(secret).to_bytes(4, "big") + secret + i.to_bytes(4, "big")).digest()
        mask.extend(block)
        i += 1
    mask = mask[:len(secret)]
    share_a = bytes(mask)
    share_b = bytes(s ^ m for s, m in zip(secret, mask))
    return share_a, share_b
