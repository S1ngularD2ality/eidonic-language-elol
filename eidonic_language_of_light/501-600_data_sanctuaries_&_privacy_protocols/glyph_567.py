# glyph_567.py — Secure Session Load
# -----------------------------------------------------------------------------
# ID:            567
# Pack:          Pack 006 (501–600)
# Name:          Secure Session Load
# Class:         session_security
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # unseal + parse; no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import Mapping, Any

def glyph_567(sealed: Mapping[str, bytes], *, key: bytes) -> Mapping[str, Any]:
    """
    Secure Session Load — unseal and parse a session dict.

    Returns
    -------
    Mapping[str,Any]

    Examples
    --------
    >>> s = glyph_566({'x':1}, key=b'k', nonce=b'n')['sealed']
    >>> glyph_567(s, key=b'k')['x']
    1
    """
    raw = glyph_502(dict(sealed), key=key)  # type: ignore
    return json.loads(raw.decode())
