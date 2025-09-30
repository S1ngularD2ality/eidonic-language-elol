# glyph_402.py — Capability Registry
# -----------------------------------------------------------------------------
# ID:            402
# Pack:          Pack 005 (401–500)
# Name:          Capability Registry
# Class:         registry
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, Mapping, Iterable

def glyph_402(catalog: Mapping[str, Iterable[str]]) -> Dict[str, Dict[str, bool]]:
    """
    Capability Registry — compact boolean capability table.

    Overview
    --------
    Converts {"agent": ["capA","capB",...]} into {"agent": {"capA":True,...}} for O(1) checks.

    Parameters
    ----------
    catalog : Mapping[str, Iterable[str]]
        Agent → iterable of capability names.

    Returns
    -------
    Dict[str, Dict[str, bool]]

    Examples
    --------
    >>> glyph_402({"a":["see","hear"], "b":["see"]})["a"]["hear"]
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(sum caps)
    - Space : O(sum caps)
    """
    out: Dict[str, Dict[str, bool]] = {}
    for agent, caps in catalog.items():
        out[str(agent)] = {str(c): True for c in caps}
    return out
