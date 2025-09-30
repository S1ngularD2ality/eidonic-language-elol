# glyph_594.py — Decrypt Key Vault
# -----------------------------------------------------------------------------
# ID:            594
# Pack:          Pack 006 (501–600)
# Name:          Decrypt Key Vault
# Class:         key_management
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # unseal + parse; no filesystem
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import Mapping, Dict

def glyph_594(sealed: Mapping[str, bytes], *, key: bytes) -> Dict[str, bytes]:
    """
    Decrypt Key Vault — recover name→key mapping.

    Returns
    -------
    Dict[str,bytes]
    """
    raw = glyph_502(dict(sealed), key=key)  # type: ignore
    obj = json.loads(raw.decode())
    return {k: bytes.fromhex(v) for k, v in obj.items()}
