# glyph_582.py — Decrypt API Request
# -----------------------------------------------------------------------------
# ID:            582
# Pack:          Pack 006 (501–600)
# Name:          Decrypt API Request
# Class:         protocol_gateway
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # unwrap + verify; no network I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib, hmac
from typing import Mapping, Any, Dict

def glyph_582(envelope: Mapping[str, Any], *, enc_key: bytes, mac_key: bytes) -> Dict[str, Any]:
    """
    Decrypt API Request — verify MAC and unseal canonical request body.

    Overview
    --------
    Expects {'sealed':{'nonce','ct','tag'}, 'mac':bytes}. Validates MAC over the
    sealed fields, then unseals to recover the canonical JSON request.

    Parameters
    ----------
    envelope : Mapping[str,Any]
    enc_key  : bytes
    mac_key  : bytes

    Returns
    -------
    Dict[str,Any]
        The parsed request mapping.

    Examples
    --------
    >>> raw = {'method':'GET','path':'/health','headers':{},'body':None}
    >>> import json
    >>> from hashlib import sha256
    >>> sealed = glyph_501(json.dumps(raw, sort_keys=True, separators=(",",":")).encode(), key=b'kE', nonce=b'n')  # type: ignore
    >>> mac = hmac.new(b'kM', sealed['nonce']+sealed['ct']+sealed['tag'], hashlib.sha256).digest()
    >>> req = glyph_582({'sealed':sealed,'mac':mac}, enc_key=b'kE', mac_key=b'kM')
    >>> req['path']
    '/health'

    Exceptions
    ----------
    - ValueError : if MAC fails or unseal fails.

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    sealed = dict(envelope.get("sealed", {}))
    mac = envelope.get("mac", b"")
    calc = hmac.new(mac_key, sealed.get("nonce", b"") + sealed.get("ct", b"") + sealed.get("tag", b""), hashlib.sha256).digest()
    if not hmac.compare_digest(calc, mac):
        raise ValueError("MAC mismatch")
    raw = glyph_502(sealed, key=enc_key)  # type: ignore
    return json.loads(raw.decode("utf-8"))
