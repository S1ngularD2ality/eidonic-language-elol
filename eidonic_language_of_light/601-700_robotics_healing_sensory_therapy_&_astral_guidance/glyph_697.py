# glyph_697.py — RETURN_PATH_MARKER
# -----------------------------------------------------------------------------
# ID:            697
# Pack:          Pack 007 (601–700)
# Name:          RETURN_PATH_MARKER
# Class:         guidance.navigation
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List

def glyph_697(labels: List[str]) -> Dict:
    """
    RETURN_PATH_MARKER — create a reversible breadcrumb stack.

    Overview
    --------
    Emits forward order and a computed reverse route for safe return rituals.

    Parameters
    ----------
    labels : List[str]
        Waypoint names.

    Returns
    -------
    Dict
        {"forward":[...], "return":[...]}
    """
    fw = [str(x) for x in labels]
    return {"type":"path_markers","forward":fw,"return":list(reversed(fw))}
