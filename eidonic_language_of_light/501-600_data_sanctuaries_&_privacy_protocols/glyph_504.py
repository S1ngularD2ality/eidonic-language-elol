# glyph_504.py — Hash Lock
# -----------------------------------------------------------------------------
# ID:            504
# Pack:          Pack 006 (501–600)
# Name:          Hash Lock
# Class:         hashing_fingerprints
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib

def glyph_504(data: bytes) -> str:
    """
    Hash Lock — SHA-256 fingerprint (hex).

    Overview
    --------
    Canonical stable digest for attestation and keying.

    Parameters
    ----------
    data : bytes

    Returns
    -------
    str : 64-hex characters

    Examples
    --------
    >>> glyph_504(b'abc') == 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    return hashlib.sha256(data).hexdigest()
