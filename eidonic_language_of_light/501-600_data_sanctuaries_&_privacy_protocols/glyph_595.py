# glyph_595.py — Secure Metadata
# -----------------------------------------------------------------------------
# ID:            595
# Pack:          Pack 006 (501–600)
# Name:          Secure Metadata
# Class:         data_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # seal canonical JSON
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import Mapping, Any, Dict

def glyph_595(meta: Mapping[str, Any], *, key: bytes, nonce: bytes) -> Dict[str, bytes]:
    """
    Secure Metadata — seal a small metadata mapping.

    Returns
    -------
    Dict[str,bytes]
    """
    raw = json.dumps(dict(meta), sort_keys=True, separators=(",", ":")).encode()
    return glyph_501(raw, key=key, nonce=nonce)  # type: ignore
