# glyph_401.py — Role Ledger
# -----------------------------------------------------------------------------
# ID:            401
# Pack:          Pack 005 (401–500)
# Name:          Role Ledger
# Class:         registry
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, Mapping

def glyph_401(roles: Mapping[str, str], assignment: Mapping[str, str]) -> Dict[str, str]:
    """
    Role Ledger — normalize and seal a (agent→role) assignment map.

    Overview
    --------
    Lowercases role keys, validates against a canonical vocabulary, and emits a new
    mapping of ``agent_id → role``. Unknown roles are downgraded to ``"observer"``.

    Parameters
    ----------
    roles : Mapping[str, str]
        Canonical role vocabulary, e.g., {"leader":"leader","scribe":"scribe",...}
    assignment : Mapping[str, str]
        Proposed (agent_id → role_name) mapping.

    Returns
    -------
    Dict[str, str]
        Cleaned, normalized assignment.

    Examples
    --------
    >>> glyph_401({"leader":"leader","observer":"observer"}, {"a":"Leader","b":"ghost"})
    {'a': 'leader', 'b': 'observer'}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    canon = {k.lower(): v for k, v in roles.items()}
    out: Dict[str, str] = {}
    for aid, role in assignment.items():
        out[str(aid)] = canon.get(str(role).lower(), "observer")
    return out
