# glyph_481.py — Finality Seal
# -----------------------------------------------------------------------------
# ID:            481
# Pack:          Pack 005 (401–500)
# Name:          Finality Seal
# Class:         registry
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib
from typing import Mapping, Dict

def glyph_481(record: Mapping[str, str]) -> Dict[str, str]:
    """
    Finality Seal — produce a deterministic seal over canonicalized fields.

    Overview
    --------
    Normalizes keys/values to strings, sorts by key, and hashes "k=v" pairs joined
    with '\n'. Returns {'seal': <sha256-hex>}.

    Parameters
    ----------
    record : Mapping[str,str]

    Returns
    -------
    Dict[str,str] : {'seal': hex}

    Examples
    --------
    >>> out = glyph_481({'a':'1','b':'2'}); len(out['seal']) == 64
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k log k)
    - Space : O(k)
    """
    items = [f"{str(k)}={str(v)}" for k, v in sorted(record.items())]
    seal = hashlib.sha256("\n".join(items).encode("utf-8")).hexdigest()
    return {"seal": seal}
