# glyph_573.py — Encrypt Text File
# -----------------------------------------------------------------------------
# ID:            573
# Pack:          Pack 006 (501–600)
# Name:          Encrypt Text File
# Class:         text_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # utf-8 + seal; no FS I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_573(text: str, *, key: bytes, nonce: bytes) -> Dict[str, bytes]:
    """
    Encrypt Text File — seal UTF-8 content.

    Returns
    -------
    Dict[str,bytes]

    Examples
    --------
    >>> env = glyph_573("hello", key=b'k', nonce=b'n'); set(env)>= {'ct','nonce','tag'}
    True
    """
    return glyph_501(text.encode("utf-8"), key=key, nonce=nonce)  # type: ignore
