# glyph_589.py — Secure Password Reset
# -----------------------------------------------------------------------------
# ID:            589
# Pack:          Pack 006 (501–600)
# Name:          Secure Password Reset
# Class:         policy_gate
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy + HMAC attest; no email/I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib, hmac
from typing import Mapping, Any, Dict

def glyph_589(account: Mapping[str, Any], *, policy: Mapping[str, Any], attest_key: bytes) -> Dict[str, Any]:
    """
    Secure Password Reset — deterministic policy check + attestation blob.

    Overview
    --------
    Evaluates required factors (e.g., 'has_secondary_email', 'recent_login<=X days').
    Emits {'ok':bool,'attest':bytes,'canonical':bytes}. No emails sent.

    Returns
    -------
    Dict[str,Any]
    """
    def cj(x): return json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    required = set(policy.get("require_flags", []))
    flags = set(str(f) for f in account.get("flags", []))
    ok = required.issubset(flags)
    canonical = cj({"acct": dict(account), "policy": dict(policy), "ok": ok})
    attest = hmac.new(attest_key, canonical, hashlib.sha256).digest()
    return {"ok": ok, "attest": attest, "canonical": canonical}
