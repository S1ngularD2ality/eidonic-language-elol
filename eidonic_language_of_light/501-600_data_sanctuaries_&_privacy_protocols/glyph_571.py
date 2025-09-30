# glyph_571.py — Encrypt Image
# -----------------------------------------------------------------------------
# ID:            571
# Pack:          Pack 006 (501–600)
# Name:          Encrypt Image
# Class:         media_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # treats input as opaque bytes; no image parsing
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_571(image_bytes: bytes, *, key: bytes, nonce: bytes) -> Dict[str, bytes]:
    """
    Encrypt Image — seal opaque image bytes (PNG/JPG/etc.).

    Returns
    -------
    Dict[str,bytes] : {'nonce','ct','tag'}

    Examples
    --------
    >>> env = glyph_571(b'\\x89PNG...', key=b'k', nonce=b'n'); 'ct' in env
    True
    """
    return glyph_501(image_bytes, key=key, nonce=nonce)  # type: ignore
