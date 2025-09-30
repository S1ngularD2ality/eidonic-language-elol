# glyph_587.py — Secure File Transfer
# -----------------------------------------------------------------------------
# ID:            587
# Pack:          Pack 006 (501–600)
# Name:          Secure File Transfer
# Class:         transport_envelope
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # envelope only; no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib, hmac
from typing import Mapping, Any, Dict

def glyph_587(file_bytes: bytes, meta: Mapping[str, Any], *, key: bytes, nonce: bytes, mac_key: bytes) -> Dict[str, Any]:
    """
    Secure File Transfer — sealed and MACed file envelope (logical).

    Overview
    --------
    Seals `file_bytes` with deterministic PRF stream + tag, then attaches HMAC
    over nonce|ct|tag|canonical(meta) for transport authenticity. No network I/O.

    Returns
    -------
    {'sealed': {...}, 'meta': dict, 'mac': bytes, 'sha256': str}
    """
    import json
    sealed = glyph_501(file_bytes, key=key, nonce=nonce)  # type: ignore
    meta_c = json.dumps(dict(meta), sort_keys=True, separators=(",", ":")).encode()
    mac = hmac.new(mac_key, sealed["nonce"] + sealed["ct"] + sealed["tag"] + meta_c, hashlib.sha256).digest()
    return {"sealed": sealed, "meta": dict(meta), "mac": mac, "sha256": hashlib.sha256(file_bytes).hexdigest()}
