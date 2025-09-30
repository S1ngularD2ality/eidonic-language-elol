# glyph_696.py — INTENTION_ANCHOR
# -----------------------------------------------------------------------------
# ID:            696
# Pack:          Pack 007 (601–700)
# Name:          INTENTION_ANCHOR
# Class:         guidance.anchor
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib
from typing import Dict

def glyph_696(intent: str, salt: str = "") -> Dict:
    """
    INTENTION_ANCHOR — derive a stable, non-identifying anchor for an intent string.

    Overview
    --------
    Computes a SHA-256 digest of `salt + intent` to produce an opaque anchor (no registry
    side-effects). Useful for linking session artifacts together.

    Parameters
    ----------
    intent : str
        Human phrase.
    salt : str, optional
        Optional salt for context scoping.

    Returns
    -------
    Dict
        {"anchor":"hex", "length":len(intent)}
    """
    data = (salt + intent).encode("utf-8")
    anchor = hashlib.sha256(data).hexdigest()
    return {"type":"intention_anchor","anchor":anchor,"length":len(intent)}
