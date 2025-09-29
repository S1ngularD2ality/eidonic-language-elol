# glyph_418.py — Autonomy Switch
# -----------------------------------------------------------------------------
# ID:            418
# Pack:          Pack 005 (401–500)
# Name:          Autonomy Switch
# Class:         controller
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_418(enabled: bool, manual_override: bool) -> bool:
    """
    Autonomy Switch — enable autonomy unless manual override is active.

    Overview
    --------
    Simple guard: returns True iff `enabled` and not `manual_override`.

    Parameters
    ----------
    enabled         : bool
    manual_override : bool

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_418(True, False)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return bool(enabled) and not bool(manual_override)
