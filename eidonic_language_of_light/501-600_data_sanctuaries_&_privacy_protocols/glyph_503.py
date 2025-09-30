# glyph_503.py — Anon Strip
# -----------------------------------------------------------------------------
# ID:            503
# Pack:          Pack 006 (501–600)
# Name:          Anon Strip
# Class:         privacy
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True  # pure dict transform; no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict, Iterable

def glyph_503(record: Mapping[str, Any], *, drop: Iterable[str] = (), mask: Iterable[str] = ()) -> Dict[str, Any]:
    """
    Anon Strip — remove sensitive fields and mask others.

    Overview
    --------
    Returns a copy of `record` without keys in `drop`; for keys in `mask`, replaces
    values with `'***'` (preserving key presence).

    Parameters
    ----------
    record : Mapping[str,Any]
    drop   : Iterable[str]
    mask   : Iterable[str]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_503({'name':'A','ssn':'123','city':'x'}, drop=['ssn'], mask=['name'])
    {'name': '***', 'city': 'x'}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    dset = set(drop); mset = set(mask)
    out: Dict[str, Any] = {}
    for k, v in record.items():
        if k in dset:
            continue
        out[k] = '***' if k in mset else v
    return out
