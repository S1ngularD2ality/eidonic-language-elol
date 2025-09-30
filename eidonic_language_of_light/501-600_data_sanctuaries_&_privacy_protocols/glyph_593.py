# glyph_593.py — Secure Key Vault
# -----------------------------------------------------------------------------
# ID:            593
# Pack:          Pack 006 (501–600)
# Name:          Secure Key Vault
# Class:         key_management
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # sealed map; no filesystem
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib
from typing import Mapping, Any, Dict

def glyph_593(keys: Mapping[str, bytes], *, key: bytes, nonce: bytes) -> Dict[str, Any]:
    """
    Secure Key Vault — seal a name→key map (deterministic, offline).

    Returns
    -------
    {'sealed': {...}, 'count': int, 'checksum': str}
    """
    raw = json.dumps({k: v.hex() for k, v in keys.items()}, sort_keys=True, separators=(",", ":")).encode()
    sealed = glyph_501(raw, key=key, nonce=nonce)  # type: ignore
    return {"sealed": sealed, "count": len(keys), "checksum": hashlib.sha256(raw).hexdigest()}
