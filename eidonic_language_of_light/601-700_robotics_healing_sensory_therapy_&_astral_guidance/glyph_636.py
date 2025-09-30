# glyph_636.py — LOW_POWER_HELP_MODE
# -----------------------------------------------------------------------------
# ID:            636
# Pack:          Pack 007 (601–700)
# Name:          LOW_POWER_HELP_MODE
# Class:         metrics_costing
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_636(battery_pct: float, help_requests: int) -> dict:
    """
    LOW_POWER_HELP_MODE — scale assistance under low battery while staying kind.

    Overview
    --------
    Computes a throttling factor from battery level and pending assistance load.

    Parameters
    ----------
    battery_pct   : float
        0..100
    help_requests : int
        Non-negative count of queued requests.

    Returns
    -------
    dict
        {'mode': 'reserve'|'thrifty'|'normal', 'assist_scale': float}

    Examples
    --------
    >>> out = glyph_636(15.0, 3)
    >>> out['mode'] == 'reserve' and 0.3 <= out['assist_scale'] <= 1.0
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    b = max(0.0, min(100.0, battery_pct))
    k = 1 + max(0, help_requests)
    scale = max(0.3, min(1.0, (b/100.0) * (1.2 / k)))
    mode = "reserve" if b < 20.0 else ("thrifty" if b < 40.0 else "normal")
    return {"mode": mode, "assist_scale": float(scale)}
