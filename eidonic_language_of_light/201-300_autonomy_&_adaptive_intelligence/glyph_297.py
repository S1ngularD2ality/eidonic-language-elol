# glyph_297.py — Dimensional Lock Bender
# -----------------------------------------------------------------------------
# ID:            297
# Pack:          Pack 003 (201–300)
# Name:          Dimensional Lock Bender
# Class:         control
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_297(flag: bool, *, on: float = 1.0, off: float = 0.0) -> float:
    """
    Dimensional Lock Bender — boolean gate selector.

    Overview
    --------
    Returns `on` if flag True else `off`.

    Parameters
    ----------
    flag : bool
    on   : float, optional (default: 1.0)
    off  : float, optional (default: 0.0)

    Returns
    -------
    float
        Selected value.

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return float(on if flag else off)
