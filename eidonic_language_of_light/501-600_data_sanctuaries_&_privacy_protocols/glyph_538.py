# glyph_538.py — Stealth Mode
# -----------------------------------------------------------------------------
# ID:            538
# Pack:          Pack 006 (501–600)
# Name:          Stealth Mode
# Class:         privacy_policy
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy state only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping

def glyph_538(enabled: bool, *, redact: bool = True) -> Mapping[str, bool]:
    """
    Stealth Mode — central privacy switch and redaction preference.

    Overview
    --------
    Use as a shared flag bundle for other privacy glyphs.

    Parameters
    ----------
    enabled : bool
    redact  : bool, optional (default: True)

    Returns
    -------
    Mapping[str,bool] : {'enabled': bool, 'redact': bool}

    Examples
    --------
    >>> glyph_538(True, redact=False)['enabled']
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return {"enabled": bool(enabled), "redact": bool(redact)}
