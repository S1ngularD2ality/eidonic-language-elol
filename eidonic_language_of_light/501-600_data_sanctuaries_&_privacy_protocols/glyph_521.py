# glyph_521.py — Secure Handshake
# -----------------------------------------------------------------------------
# ID:            521
# Pack:          Pack 006 (501–600)
# Name:          Secure Handshake
# Class:         protocol
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # PSK-based; no RNG, no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib, hmac, json
from typing import Mapping, Any, Dict

def glyph_521(client_hello: Mapping[str, Any],
              server_hello: Mapping[str, Any],
              *,
              pre_shared_key: bytes,
              transcript_binding: bytes = b"") -> Dict[str, bytes]:
    """
    Secure Handshake — derive symmetric session keys from client/server hellos.

    Overview
    --------
    Educational PSK handshake: canonically hash hellos, bind optional transcript,
    and derive deterministic keys via HMAC-SHA256. Outputs session id and two keys.

    Parameters
    ----------
    client_hello       : Mapping[str,Any]
    server_hello       : Mapping[str,Any]
    pre_shared_key     : bytes
    transcript_binding : bytes, optional

    Returns
    -------
    Dict[str,bytes] : {'sid': bytes, 'k_enc': bytes, 'k_mac': bytes}

    Examples
    --------
    >>> out = glyph_521({'v':1},{'v':1}, pre_shared_key=b'K')
    >>> len(out['k_enc']) == 32 and len(out['k_mac']) == 32
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)  (serialization cost)
    - Space : O(1)
    """
    def cj(x): return json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    h = hashlib.sha256
    ch = h(cj(client_hello)).digest()
    sh = h(cj(server_hello)).digest()
    sid = h(ch + sh).digest()
    prk = hmac.new(pre_shared_key, b"PRK"+ch+sh+transcript_binding, h).digest()
    k_enc = hmac.new(prk, b"enc"+sid, h).digest()
    k_mac = hmac.new(prk, b"mac"+sid, h).digest()
    return {"sid": sid, "k_enc": k_enc, "k_mac": k_mac}
