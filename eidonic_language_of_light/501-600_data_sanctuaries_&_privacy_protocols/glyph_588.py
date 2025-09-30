# glyph_588.py — Decrypt File Transfer
# -----------------------------------------------------------------------------
# ID:            588
# Pack:          Pack 006 (501–600)
# Name:          Decrypt File Transfer
# Class:         transport_envelope
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # unwrap; no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib, hmac
from typing import Mapping, Any

def glyph_588(envelope: Mapping[str, Any], *, key: bytes, mac_key: bytes) -> bytes:
    """
    Decrypt File Transfer — verify MAC, unseal bytes, and integrity-check.

    Returns
    -------
    bytes

    Examples
    --------
    >>> env = glyph_587(b'x', {'name':'a'}, key=b'k', nonce=b'n', mac_key=b'm')
    >>> glyph_588(env, key=b'k', mac_key=b'm')
    b'x'
    """
    sealed = dict(envelope.get("sealed", {}))
    meta = envelope.get("meta", {})
    mac = envelope.get("mac", b"")
    meta_c = json.dumps(dict(meta), sort_keys=True, separators=(",", ":")).encode()
    calc = hmac.new(mac_key, sealed["nonce"] + sealed["ct"] + sealed["tag"] + meta_c, hashlib.sha256).digest()
    if not hmac.compare_digest(calc, mac):
        raise ValueError("MAC mismatch")
    raw = glyph_502(sealed, key=key)  # type: ignore
    # optional checksum comparison if present
    expected = envelope.get("sha256")
    if isinstance(expected, str):
        if hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError("payload checksum mismatch")
    return raw
