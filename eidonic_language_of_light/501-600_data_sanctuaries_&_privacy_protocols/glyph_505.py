# glyph_505.py — Salt Hash
# -----------------------------------------------------------------------------
# ID:            505
# Pack:          Pack 006 (501–600)
# Name:          Salt Hash
# Class:         hashing_fingerprints
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # given inputs; no RNG here
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib

def glyph_505(data: bytes, *, salt: bytes) -> str:
    """
    Salt Hash — SHA-256(salt || data) hex.

    Overview
    --------
    Simple salted fingerprint for de-duplication or lookup tables.

    Parameters
    ----------
    data : bytes
    salt : bytes

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_505(b'abc', salt=b'x') == glyph_505(b'abc', salt=b'x')
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    return hashlib.sha256(salt + data).hexdigest()
