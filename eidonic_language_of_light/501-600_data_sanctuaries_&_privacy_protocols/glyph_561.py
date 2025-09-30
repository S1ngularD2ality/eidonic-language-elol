# glyph_561.py — Dual Layer Hash
# -----------------------------------------------------------------------------
# ID:            561
# Pack:          Pack 006 (501–600)
# Name:          Dual Layer Hash
# Class:         hashing_fingerprints
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure hashing; no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib
from typing import Tuple

def glyph_561(data: bytes, *, salt: bytes = b"") -> Tuple[str, str]:
    """
    Dual Layer Hash — compute (sha256, sha512) with optional salted domain separation.

    Overview
    --------
    Returns a tuple of hex digests: (SHA-256(salt||data), SHA-512(salt||data)).

    Parameters
    ----------
    data : bytes
    salt : bytes, optional (default: ``b""``)

    Returns
    -------
    (str, str) : (sha256_hex, sha512_hex)

    Examples
    --------
    >>> h256, h512 = glyph_561(b"abc")
    >>> len(h256), len(h512)
    (64, 128)

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    d = salt + data
    return hashlib.sha256(d).hexdigest(), hashlib.sha512(d).hexdigest()
