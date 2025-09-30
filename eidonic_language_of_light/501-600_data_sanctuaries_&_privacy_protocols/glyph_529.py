# glyph_529.py — Mask Email
# -----------------------------------------------------------------------------
# ID:            529
# Pack:          Pack 006 (501–600)
# Name:          Mask Email
# Class:         masking_anonymization
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_529(addr: str) -> str:
    """
    Mask Email — keep first/last character of local part; mask middle.

    Overview
    --------
    Returns '***' for invalid addresses.

    Parameters
    ----------
    addr : str

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_529("alice@example.com")
    'a***e@example.com'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    if "@" not in addr:
        return "***"
    local, domain = addr.split("@", 1)
    if len(local) <= 2:
        masked = local[0:1] + "*"
    else:
        masked = local[0] + "***" + local[-1]
    return masked + "@" + domain
