# glyph_592.py — Decrypt Cache
# -----------------------------------------------------------------------------
# ID:            592
# Pack:          Pack 006 (501–600)
# Name:          Decrypt Cache
# Class:         data_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # unseal + parse; no storage
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import Mapping, Any

def glyph_592(sealed: Mapping[str, bytes], *, key: bytes) -> Mapping[str, Any]:
    """
    Decrypt Cache — restore canonical JSON cache entry.

    Returns
    -------
    Mapping[str,Any]
    """
    raw = glyph_502(dict(sealed), key=key)  # type: ignore
    return json.loads(raw.decode())
