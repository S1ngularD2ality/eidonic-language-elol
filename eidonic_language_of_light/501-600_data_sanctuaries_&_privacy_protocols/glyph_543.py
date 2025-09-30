# glyph_543.py — Multi Key Encrypt
# -----------------------------------------------------------------------------
# ID:            543
# Pack:          Pack 006 (501–600)
# Name:          Multi Key Encrypt
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Iterable
import hashlib

def _derive(key: bytes) -> bytes:
    return hashlib.sha256(key).digest()

def glyph_543(data: bytes, keys: Iterable[bytes]) -> bytes:
    """
    Multi Key Encrypt — cascade XOR with multiple derived key streams.

    Overview
    --------
    Deterministically derives a 32-byte stream per key (SHA-256) and XORs them over
    the payload in order. This is a **toy** envelope for composition/testing in Elol;
    not a substitute for AEAD. Use with `glyph_544` for reversal.

    Parameters
    ----------
    data : bytes
        Payload bytes.
    keys : Iterable[bytes]
        One or more key materials.

    Returns
    -------
    bytes
        Transformed bytes.

    Examples
    --------
    >>> c = glyph_543(b"secret", [b"k1", b"k2"])
    >>> glyph_544(c, [b"k1", b"k2"]) == b"secret"
    True

    Exceptions
    ----------
    - ValueError : if no keys are provided.

    Complexity
    ----------
    - Time  : O(N · K)
    - Space : O(N)
    """
    ks = list(keys)
    if not ks:
        raise ValueError("at least one key is required")
    out = bytearray(data)
    for k in ks:
        stream = _derive(k)
        for i in range(len(out)):
            out[i] ^= stream[i % len(stream)]
    return bytes(out)
