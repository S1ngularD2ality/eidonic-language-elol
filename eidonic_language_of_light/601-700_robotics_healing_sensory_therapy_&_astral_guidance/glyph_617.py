# glyph_617.py — HANDSHAKE_PROTOCOL
# -----------------------------------------------------------------------------
# ID:            617
# Pack:          Pack 007 (601–700)
# Name:          HANDSHAKE_PROTOCOL
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # deterministic transcript generator
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict
import json, hashlib

def glyph_617(peer_a: Mapping[str, Any], peer_b: Mapping[str, Any]) -> Dict[str, Any]:
    """
    HANDSHAKE_PROTOCOL — create a symmetric handshake transcript.

    Returns
    -------
    {'transcript': bytes, 'hash': str}
    """
    a = json.dumps(dict(peer_a), sort_keys=True, separators=(",", ":")).encode()
    b = json.dumps(dict(peer_b), sort_keys=True, separators=(",", ":")).encode()
    t = b"ELoL-HS1|" + a + b"|" + b + b"|ELoL-HS1"
    return {"transcript": t, "hash": hashlib.sha256(t).hexdigest()}
