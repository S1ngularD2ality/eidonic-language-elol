# glyph_510.py — Token Validate
# -----------------------------------------------------------------------------
# ID:            510
# Pack:          Pack 006 (501–600)
# Name:          Token Validate
# Class:         auth_access_control
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # struct + HMAC integrity
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hmac, hashlib
from typing import Mapping, Any

def glyph_510(token: Mapping[str, Any], *, key: bytes) -> bool:
    """
    Token Validate — verify `sig == HMAC(key, canonical_json(header,claims))`.

    Overview
    --------
    Expects token with fields: {'hdr': {...}, 'claims': {...}, 'sig': bytes}.

    Parameters
    ----------
    token : Mapping[str,Any]
    key   : bytes

    Returns
    -------
    bool

    Examples
    --------
    >>> t = {'hdr':{'alg':'HS256'}, 'claims':{'sub':'a'}, 'sig':b''}
    >>> raw = json.dumps({'hdr':t['hdr'],'claims':t['claims']}, sort_keys=True).encode()
    >>> t['sig'] = hmac.new(b'k', raw, hashlib.sha256).digest()
    >>> glyph_510(t, key=b'k')
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    raw = json.dumps({"hdr": token.get("hdr", {}), "claims": token.get("claims", {})},
                     sort_keys=True, separators=(",", ":")).encode()
    sig = token.get("sig", b"")
    calc = hmac.new(key, raw, hashlib.sha256).digest()
    return isinstance(sig, (bytes, bytearray)) and hmac.compare_digest(sig, calc)
