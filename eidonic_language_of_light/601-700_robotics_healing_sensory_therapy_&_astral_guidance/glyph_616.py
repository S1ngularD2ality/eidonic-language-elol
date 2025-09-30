# glyph_616.py — REMOTE_ASSIST_CONNECT
# -----------------------------------------------------------------------------
# ID:            616
# Pack:          Pack 007 (601–700)
# Name:          REMOTE_ASSIST_CONNECT
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # envelope only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict
import json, hashlib, hmac

def glyph_616(snapshot: Mapping[str, Any], *, key: bytes) -> Dict[str, Any]:
    """
    REMOTE_ASSIST_CONNECT — produce a signed assist request envelope.

    Returns
    -------
    {'canonical': bytes, 'mac': bytes}
    """
    canon = json.dumps(dict(snapshot), sort_keys=True, separators=(",", ":")).encode()
    tag = hmac.new(key, canon, hashlib.sha256).digest()
    return {"canonical": canon, "mac": tag}
