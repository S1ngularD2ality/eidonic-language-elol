# glyph_692.py — ASTRAL_GUIDE_ACTIVATE
# -----------------------------------------------------------------------------
# ID:            692
# Pack:          Pack 007 (601–700)
# Name:          ASTRAL_GUIDE_ACTIVATE
# Class:         guidance.astral
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_692(intent: str, level: str = "gentle") -> Dict:
    """
    ASTRAL_GUIDE_ACTIVATE — initialize an astral guidance session frame.

    Overview
    --------
    Emits a **symbolic session header** with intent, safeguards, and a seed for subsequent
    astral glyphs. No metaphysical claims—pure structured metadata for downstream tools.

    Parameters
    ----------
    intent : str
        Human-readable purpose statement.
    level : str, optional
        Guidance intensity label.

    Returns
    -------
    Dict
        Session header with safeguards.
    """
    return {
        "type":"astral_session",
        "intent": intent.strip(),
        "level": level,
        "safety": {"consent": True, "grounding_required": True, "timeout_s": 900}
    }
