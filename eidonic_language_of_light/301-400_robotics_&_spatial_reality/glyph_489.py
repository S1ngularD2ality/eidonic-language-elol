# glyph_489.py — Gossip Bloom
# -----------------------------------------------------------------------------
# ID:            489
# Pack:          Pack 005 (401–500)
# Name:          Gossip Bloom
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib
from typing import Sequence, List

def glyph_489(keys: Sequence[str], *, m_bits: int = 1024, k_hashes: int = 3) -> List[int]:
    """
    Gossip Bloom — build a compact bloom filter bitset indices.

    Overview
    --------
    Returns the set-bit positions for all keys using k_hashes SHA-256 variants.

    Parameters
    ----------
    keys     : Sequence[str]
    m_bits   : int, optional (default: 1024)
    k_hashes : int, optional (default: 3)

    Returns
    -------
    List[int] : indices in [0, m_bits)

    Examples
    --------
    >>> idxs = glyph_489(['a','b'], m_bits=16, k_hashes=2); all(0 <= i < 16 for i in idxs)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k·n)
    - Space : O(k·n)
    """
    out: List[int] = []
    for key in keys:
        base = hashlib.sha256(str(key).encode()).digest()
        for j in range(k_hashes):
            h = hashlib.sha256(base + bytes([j])).hexdigest()
            out.append(int(h, 16) % int(m_bits))
    return sorted(set(out))
