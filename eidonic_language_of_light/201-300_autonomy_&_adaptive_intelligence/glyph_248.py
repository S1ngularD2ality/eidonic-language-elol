# glyph_248.py — Anchor Field Gatekeeper
# -----------------------------------------------------------------------------
# ID:            248
# Pack:          Pack 003 (201–300)
# Name:          Anchor Field Gatekeeper
# Class:         control
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Callable, Iterable, TypeVar, List
T = TypeVar("T")

def glyph_248(items: Iterable[T], *, allow: Callable[[T], bool]) -> List[T]:
    """
    Anchor Field Gatekeeper — filter by deterministic predicate.

    Overview
    --------
    Passes only elements for which `allow(x)` is True.

    Parameters
    ----------
    items : Iterable[T]
    allow : Callable[[T], bool]

    Returns
    -------
    List[T]
        Allowed items.

    Examples
    --------
    >>> glyph_248([1,2,3,4], allow=lambda x: x%2==0)
    [2, 4]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    return [x for x in items if allow(x)]
