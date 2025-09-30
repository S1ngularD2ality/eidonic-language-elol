# glyph_463.py — Token Budgeter
# -----------------------------------------------------------------------------
# ID:            463
# Pack:          Pack 005 (401–500)
# Name:          Token Budgeter
# Class:         allocator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Dict

def glyph_463(requests: Mapping[str, int], *, budget: int) -> Dict[str, int]:
    """
    Token Budgeter — proportional allocation with floor of zero.

    Overview
    --------
    Distributes integer `budget` across requestors in proportion to requested tokens.

    Parameters
    ----------
    requests : Mapping[agent_id, requested_tokens]
    budget   : int

    Returns
    -------
    Dict[str, int] : agent_id → granted_tokens

    Examples
    --------
    >>> glyph_463({"a":10,"b":30}, budget=20)
    {'a': 5, 'b': 15}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    total = sum(int(v) for v in requests.values())
    if total <= 0 or budget <= 0:
        return {k: 0 for k in requests}
    out = {k: int(budget * (int(v) / total)) for k, v in requests.items()}
    # distribute remainder by largest fractional part
    used = sum(out.values())
    rem = budget - used
    if rem > 0:
        fracs = sorted(((k, (int(v) / total) * budget - out[k]) for k, v in requests.items()),
                       key=lambda kv: -kv[1])
        for i in range(rem):
            out[fracs[i % len(fracs)][0]] += 1
    return out
