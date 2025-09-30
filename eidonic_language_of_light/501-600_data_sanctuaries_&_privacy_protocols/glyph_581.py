# glyph_581.py — Secure API Gateway
# -----------------------------------------------------------------------------
# ID:            581
# Pack:          Pack 006 (501–600)
# Name:          Secure API Gateway
# Class:         protocol_gateway
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # canonicalize + policy + HMAC; no network I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib, hmac
from typing import Mapping, Any, Dict

def glyph_581(request: Mapping[str, Any], *, policy: Mapping[str, Any], mac_key: bytes) -> Dict[str, Any]:
    """
    Secure API Gateway — validate a canonical request against a static policy and MAC it.

    Overview
    --------
    Canonicalize the request, evaluate allow/deny rules from `policy`, and emit
    a deterministic gateway envelope containing decision and an HMAC over the
    canonical request. No network side effects.

    Parameters
    ----------
    request : Mapping[str,Any]
        Expected keys: 'method':str, 'path':str, 'headers':dict, 'body':Any (JSON-serializable).
    policy  : Mapping[str,Any]
        Example: {'allow_paths': ['/health','/status'], 'allow_methods': ['GET','POST']}.
    mac_key : bytes
        Secret key used to produce integrity MAC over the canonical form.

    Returns
    -------
    Dict[str,Any]
        {'decision':'allow'|'deny','mac':bytes,'canonical':bytes}

    Examples
    --------
    >>> env = glyph_581({'method':'GET','path':'/health','headers':{},'body':None},
    ...                 policy={'allow_paths':['/health'],'allow_methods':['GET']},
    ...                 mac_key=b'k')
    >>> env['decision']
    'allow'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n) (canonicalization)
    - Space : O(n)
    """
    def canon(x) -> bytes:
        return json.dumps(x, sort_keys=True, separators=(",", ":")).encode("utf-8")

    allow_paths = set(policy.get("allow_paths", []))
    allow_methods = set(policy.get("allow_methods", []))
    method = str(request.get("method", "")).upper()
    path = str(request.get("path", ""))

    decision = "allow" if (path in allow_paths and method in allow_methods) else "deny"
    canonical = canon({"method": method, "path": path, "headers": request.get("headers", {}),
                       "body": request.get("body", None)})

    mac = hmac.new(mac_key, canonical, hashlib.sha256).digest()
    return {"decision": decision, "mac": mac, "canonical": canonical}
