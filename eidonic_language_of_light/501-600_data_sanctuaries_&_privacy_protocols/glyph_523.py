# glyph_523.py — Safe Channel
# -----------------------------------------------------------------------------
# ID:            523
# Pack:          Pack 006 (501–600)
# Name:          Safe Channel
# Class:         transport_envelope
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # deterministic sealing and MAC
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib, hmac
from typing import Mapping, Any, Dict

def glyph_523(payload: Mapping[str, Any], *, k_enc: bytes, k_mac: bytes, nonce: bytes) -> Dict[str, Any]:
    """
    Safe Channel — integrity-wrapped sealed JSON payload.

    Overview
    --------
    Canonicalize JSON, seal with `Data Seal` semantics, and attach HMAC over the
    envelope for transport authenticity.

    Parameters
    ----------
    payload : Mapping[str,Any]
    k_enc   : bytes
    k_mac   : bytes
    nonce   : bytes

    Returns
    -------
    Dict[str,Any] : {'sealed': {'nonce','ct','tag'}, 'mac': bytes}

    Examples
    --------
    >>> env = glyph_523({'a':1}, k_enc=b'e', k_mac=b'm', nonce=b'n')
    >>> isinstance(env['mac'], (bytes, bytearray))
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    raw = json.dumps(dict(payload), sort_keys=True, separators=(",", ":")).encode()
    sealed = glyph_501(raw, key=k_enc, nonce=nonce)  # type: ignore
    mac = hmac.new(k_mac, sealed["nonce"] + sealed["ct"] + sealed["tag"], hashlib.sha256).digest()
    return {"sealed": sealed, "mac": mac}
