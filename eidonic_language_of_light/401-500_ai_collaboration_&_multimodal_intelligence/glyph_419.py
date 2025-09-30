# glyph_419.py — Modal Bridge
# -----------------------------------------------------------------------------
# ID:            419
# Pack:          Pack 005 (401–500)
# Name:          Modal Bridge
# Class:         translator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_419(packet: Mapping[str, Any], *, to: str) -> Dict[str, Any]:
    """
    Modal Bridge — normalize a {mode,data} packet into target-mode metadata.

    Overview
    --------
    Produces a shallow wrapper: {'mode': to, 'data': packet['data'], 'meta': {'src_mode': packet['mode']}}.

    Parameters
    ----------
    packet : Mapping[str,Any]  (expects 'mode','data')
    to     : str

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_419({'mode':'text','data':'hi'}, to='vision')['meta']['src_mode']
    'text'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return {"mode": str(to), "data": packet.get("data"), "meta": {"src_mode": str(packet.get("mode", "unknown"))}}
