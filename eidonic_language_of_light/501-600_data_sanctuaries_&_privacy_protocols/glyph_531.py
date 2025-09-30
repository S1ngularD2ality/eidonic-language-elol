# glyph_531.py — Secure Time Sync
# -----------------------------------------------------------------------------
# ID:            531
# Pack:          Pack 006 (501–600)
# Name:          Secure Time Sync
# Class:         protocol
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure arithmetic
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Tuple

def glyph_531(t_client_send: int, t_server_recv: int, t_server_send: int, t_client_recv: int) -> Tuple[int, int]:
    """
    Secure Time Sync — compute (offset, delay) à la NTP-style without network.

    Overview
    --------
    offset = ((T2 − T1) + (T3 − T4))//2 ; delay = (T4 − T1) − (T3 − T2).

    Parameters
    ----------
    t_client_send : int  (T1)
    t_server_recv : int  (T2)
    t_server_send : int  (T3)
    t_client_recv : int  (T4)

    Returns
    -------
    Tuple[int,int] : (offset, delay)

    Examples
    --------
    >>> glyph_531(0, 5, 6, 12)
    ( -1, 1 )

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    offset = ((t_server_recv - t_client_send) + (t_server_send - t_client_recv)) // 2
    delay  = (t_client_recv - t_client_send) - (t_server_send - t_server_recv)
    return int(offset), int(delay)
