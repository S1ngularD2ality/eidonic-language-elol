# glyph_590.py — Validate Password Reset
# -----------------------------------------------------------------------------
# ID:            590
# Pack:          Pack 006 (501–600)
# Name:          Validate Password Reset
# Class:         policy_gate
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # HMAC verify
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hmac, hashlib
from typing import Mapping, Any

def glyph_590(attestation: Mapping[str, Any], *, key: bytes) -> bool:
    """
    Validate Password Reset — verify attestation blob from glyph_589.

    Returns
    -------
    bool
    """
    calc = hmac.new(key, attestation.get("canonical", b""), hashlib.sha256).digest()
    return hmac.compare_digest(calc, attestation.get("attest", b""))
