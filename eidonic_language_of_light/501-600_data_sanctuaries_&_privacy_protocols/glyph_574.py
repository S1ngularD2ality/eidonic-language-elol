# glyph_574.py — Decrypt Text File
# -----------------------------------------------------------------------------
# ID:            574
# Pack:          Pack 006 (501–600)
# Name:          Decrypt Text File
# Class:         text_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # unseal + decode; no FS I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_574(sealed: dict, *, key: bytes) -> str:
    """
    Decrypt Text File — unseal and decode UTF-8 text.

    Returns
    -------
    str

    Examples
    --------
    >>> s = glyph_573("x", key=b'k', nonce=b'n'); glyph_574(s, key=b'k')
    'x'
    """
    raw = glyph_502(sealed, key=key)  # type: ignore
    return raw.decode("utf-8")
