# glyph_410.py — Role Switch
# -----------------------------------------------------------------------------
# ID:            410
# Pack:          Pack 005 (401–500)
# Name:          Role Switch
# Class:         controller
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Dict

def glyph_410(state: Mapping[str, str], agent: str, new_role: str) -> Dict[str, str]:
    """
    Role Switch — immutably set an agent's role.

    Overview
    --------
    Copies the mapping and assigns ``state[agent] = new_role`` in the copy.

    Parameters
    ----------
    state    : Mapping[str,str]
    agent    : str
    new_role : str

    Returns
    -------
    Dict[str,str]

    Examples
    --------
    >>> glyph_410({"a":"leader"}, "a", "scribe")["a"]
    'scribe'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    out = dict(state)
    out[str(agent)] = str(new_role)
    return out
