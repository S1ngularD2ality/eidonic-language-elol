# glyph_694.py — ASTRAL_PROTECT_FIELD
# -----------------------------------------------------------------------------
# ID:            694
# Pack:          Pack 007 (601–700)
# Name:          ASTRAL_PROTECT_FIELD
# Class:         guidance.protection
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List

def glyph_694(layers: List[Dict] | None = None, level: str = "gentle") -> Dict:
    """
    ASTRAL_PROTECT_FIELD — construct a layered protective field spec.

    Overview
    --------
    Produces symbolic layers like "boundary", "purify", "stabilize" with weights that
    sum to 1. Consumers may render as audio/visual/ritual cues.

    Parameters
    ----------
    layers : List[Dict], optional
        [{"name":"boundary","weight":0.5}, ...]
    level : str, optional
        Intensity label.

    Returns
    -------
    Dict
        Normalized layer plan.
    """
    layers = layers or [{"name":"boundary","weight":0.5},{"name":"purify","weight":0.3},{"name":"stabilize","weight":0.2}]
    total = sum(float(l["weight"]) for l in layers)
    if total <= 0: raise ValueError("sum of weights must be > 0")
    norm = [{"name":str(l["name"]), "weight": float(l["weight"])/total} for l in layers]
    return {"type":"protect_field","level":level,"layers":norm}
