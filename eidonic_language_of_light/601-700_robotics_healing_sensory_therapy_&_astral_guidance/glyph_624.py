# glyph_624.py — CHILD_SAFETY_MODE
# -----------------------------------------------------------------------------
# ID:            624
# Pack:          Pack 007 (601–700)
# Name:          CHILD_SAFETY_MODE
# Class:         human_care_ethics
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_624(context: Mapping[str, Any]) -> Dict[str, Any]:
    """
    CHILD_SAFETY_MODE — derive movement/force caps for child-present contexts.

    Overview
    --------
    Etiquette rules to reduce speed and force when children or tight spaces are present.

    Parameters
    ----------
    context : Mapping[str, Any]
        Keys: 'child_present': bool, 'crowd_level': float (0..1), 'space_tight': bool

    Returns
    -------
    Dict[str, Any]
        {'speed_scale': float, 'force_cap_n': float, 'mode': str}

    Examples
    --------
    >>> glyph_624({'child_present': True, 'crowd_level': 0.2, 'space_tight': False})['mode']
    'child_guard'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    child = bool(context.get("child_present", False))
    crowd = max(0.0, min(1.0, float(context.get("crowd_level", 0.0))))
    tight = bool(context.get("space_tight", False))
    scale = 0.5 if child else (0.7 if (crowd > 0.5 or tight) else 1.0)
    cap = 8.0 if child else (12.0 if (crowd > 0.5 or tight) else 20.0)
    return {"speed_scale": scale, "force_cap_n": cap, "mode": "child_guard" if child else "standard"}
