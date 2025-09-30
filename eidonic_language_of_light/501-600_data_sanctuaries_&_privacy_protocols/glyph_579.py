# glyph_579.py — Decrypt Database
# -----------------------------------------------------------------------------
# ID:            579
# Pack:          Pack 006 (501–600)
# Name:          Decrypt Database
# Class:         data_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # unseal + parse; no DB I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import List, Dict, Any, Mapping

def glyph_579(sealed: Mapping[str, bytes], *, key: bytes) -> List[Dict[str, Any]]:
    """
    Decrypt Database — unseal and parse list of row dicts.

    Returns
    -------
    List[Dict[str,Any]]

    Examples
    --------
    >>> env = glyph_578([{'x':1}], key=b'k', nonce=b'n')
    >>> glyph_579(env, key=b'k')[0]['x']
    1
    """
    raw = glyph_502(dict(sealed), key=key)  # type: ignore
    return json.loads(raw.decode())
