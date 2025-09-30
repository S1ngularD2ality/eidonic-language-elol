# glyph_676.py — ENERGY_SHARE_PROTOCOL
# -----------------------------------------------------------------------------
# ID:            676
# Pack:          Pack 007 (601–700)
# Name:          ENERGY_SHARE_PROTOCOL
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # arithmetic only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_676(donors_pct: list[float], receivers_need: list[float]) -> dict:
    """
    ENERGY_SHARE_PROTOCOL — compute a fair share vector from donors to receivers.

    Overview
    --------
    Normalizes donor surplus and receiver need, then allocates proportionally.

    Parameters
    ----------
    donors_pct : list[float]     # battery %
    receivers_need : list[float] # desired %

    Returns
    -------
    {'alloc': List[List[float]]}  # matrix alloc[receiver][donor] in percent units

    Examples
    --------
    >>> A = glyph_676([80, 90], [30, 20])['alloc']
    >>> len(A) == 2 and len(A[0]) == 2
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(R·D)
    - Space : O(R·D)
    """
    import math
    donors = [max(0.0, d - 60.0) for d in donors_pct]  # surplus above 60%
    need = [max(0.0, 60.0 - r) for r in receivers_need]  # need up to 60%
    ds = sum(donors) or 1.0
    rs = sum(need) or 1.0
    # If donors < need, just scale; else receivers get their full need proportionally
    scale = min(1.0, ds / rs)
    alloc = []
    for rn in need:
        row = []
        for dd in donors:
            row.append((rn*scale) * (dd/ds) if ds > 0 else 0.0)
        alloc.append(row)
    return {"alloc": alloc}
