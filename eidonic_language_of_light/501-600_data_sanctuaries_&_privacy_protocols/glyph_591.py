# glyph_591.py — Secure Cache
# -----------------------------------------------------------------------------
# ID:            591
# Pack:          Pack 006 (501–600)
# Name:          Secure Cache
# Class:         data_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # seal-only; no storage
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import Mapping, Any, Dict

def glyph_591(record: Mapping[str, Any], *, key: bytes, nonce: bytes) -> Dict[str, bytes]:
    """
    Secure Cache — sealed canonical JSON for cache entries (logical).

    Returns
    -------
    Dict[str,bytes] : {'nonce','ct','tag'}
    """
    raw = json.dumps(dict(record), sort_keys=True, separators=(",", ":")).encode()
    return glyph_501(raw, key=key, nonce=nonce)  # type: ignore
