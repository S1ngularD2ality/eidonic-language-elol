# glyph_572.py — Decrypt Image
# -----------------------------------------------------------------------------
# ID:            572
# Pack:          Pack 006 (501–600)
# Name:          Decrypt Image
# Class:         media_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # unseal bytes; no image parsing
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_572(sealed: dict, *, key: bytes) -> bytes:
    """
    Decrypt Image — unseal opaque image bytes.

    Returns
    -------
    bytes

    Examples
    --------
    >>> raw = glyph_572(glyph_571(b'img', key=b'k', nonce=b'n'), key=b'k')
    >>> raw == b'img'
    True
    """
    return glyph_502(sealed, key=key)  # type: ignore
