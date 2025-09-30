# glyph_629.py — ASSISTIVE_HANDOFF
# -----------------------------------------------------------------------------
# ID:            629
# Pack:          Pack 007 (601–700)
# Name:          ASSISTIVE_HANDOFF
# Class:         manipulation_gentle
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_629(approach_speed: float, *,
              dwell_s: float = 1.0, release_scale: float = 0.4) -> Dict[str, float]:
    """
    ASSISTIVE_HANDOFF — compute soften→dwell→release cadence.

    Overview
    --------
    Derives a gentle handoff timing profile from approach speed.

    Parameters
    ----------
    approach_speed : float
        Relative approach speed (m/s).
    dwell_s : float, optional (default: ``1.0``)
        Hold time at handoff.
    release_scale : float, optional (default: ``0.4``)
        Softening factor in [0,1].

    Returns
    -------
    Dict[str, float]
        {'t_soften': float, 't_dwell': float, 'release_scale': float}

    Examples
    --------
    >>> out = glyph_629(0.5)
    >>> 0.2 <= out['t_soften'] <= 2.0
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    t_soft = max(0.2, min(2.0, 0.5 / max(0.1, approach_speed)))
    return {"t_soften": t_soft, "t_dwell": max(0.2, dwell_s), "release_scale": max(0.1, min(1.0, release_scale))}
