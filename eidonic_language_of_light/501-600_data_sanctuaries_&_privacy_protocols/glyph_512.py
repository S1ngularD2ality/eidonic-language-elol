# glyph_512.py — Decrypt File
# -----------------------------------------------------------------------------
# ID:            512
# Pack:          Pack 006 (501–600)
# Name:          Decrypt File
# Class:         crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True  # no filesystem I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_512(sealed: dict, *, key: bytes) -> bytes:
    """
    Decrypt File — unwrap sealed bytestream.

    Overview
    --------
    Alias of `Data Unseal` specialized for file-like payloads.

    Parameters
    ----------
    sealed : dict
    key    : bytes

    Returns
    -------
    bytes

    Examples
    --------
    >>> s = glyph_511(b'x', key=b'k', nonce=b'n')
    >>> glyph_512(s, key=b'k')
    b'x'

    Exceptions
    ----------
    - ValueError : if authentication fails.

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    return glyph_502(sealed, key=key)  # type: ignore
