# glyph_544.py — Multi Key Decrypt
# -----------------------------------------------------------------------------
# ID:            544
# Pack:          Pack 006 (501–600)
# Name:          Multi Key Decrypt
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

# XOR cascade is its own inverse; same as glyph_543
def glyph_544(data: bytes, keys: Iterable[bytes]) -> bytes:
    """
    Multi Key Decrypt — reverse the multi-key XOR cascade.

    Overview
    --------
    Because XOR is involutive, applying the same cascade with the **same key order**
    restores the original.

    Parameters
    ----------
    data : bytes
        Encrypted bytes.
    keys : Iterable[bytes]
        The same keys used in `glyph_543`, in the same order.

    Returns
    -------
    bytes
        Original bytes.

    Examples
    --------
    >>> glyph_544(glyph_543(b"x", [b"a"]), [b"a"]) == b"x"
    True

    Exceptions
    ----------
    - ValueError : if no keys are provided.

    Complexity
    ----------
    - Time  : O(N · K)
    - Space : O(N)
    """
    # reuse implementation by importing locally to avoid cycle
    from hashlib import sha256
    ks = list(keys)
    if not ks:
        raise ValueError("at least one key is required")
    out = bytearray(data)
    for k in ks:
        stream = sha256(k).digest()
        for i in range(len(out)):
            out[i] ^= stream[i % len(stream)]
    return bytes(out)
