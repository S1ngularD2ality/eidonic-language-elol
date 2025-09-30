# glyph_535.py — Firewall Rule
# -----------------------------------------------------------------------------
# ID:            535
# Pack:          Pack 006 (501–600)
# Name:          Firewall Rule
# Class:         policy_gate
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure predicate
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Set

def glyph_535(src_ip: str, dst_port: int, *, allow_ips: Set[str], allow_ports: Set[int]) -> bool:
    """
    Firewall Rule — allow-list predicate over source IP and destination port.

    Overview
    --------
    Returns True iff both IP and port are present in their respective allow sets.

    Parameters
    ----------
    src_ip     : str
    dst_port   : int
    allow_ips  : Set[str]
    allow_ports: Set[int]

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_535('1.2.3.4', 443, allow_ips={'1.2.3.4'}, allow_ports={80,443})
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1) average
    - Space : O(1)
    """
    return (src_ip in allow_ips) and (int(dst_port) in allow_ports)
