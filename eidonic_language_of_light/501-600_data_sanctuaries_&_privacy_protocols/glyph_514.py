# glyph_514.py — Privacy Mode
# -----------------------------------------------------------------------------
# ID:            514
# Pack:          Pack 006 (501–600)
# Name:          Privacy Mode
# Class:         masking_anonymization
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy gate only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_514(enabled: bool, *, require_consent: bool, has_consent: bool) -> bool:
    """
    Privacy Mode — allow processing only when enabled and consent satisfied.

    Overview
    --------
    Returns True iff `enabled` and (not require_consent or has_consent).

    Parameters
    ----------
    enabled        : bool
    require_consent: bool
    has_consent    : bool

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_514(True, require_consent=True, has_consent=False)
    False

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return bool(enabled) and (not require_consent or bool(has_consent))
