# glyph_113.py — Soul Code Invoker
# -----------------------------------------------------------------------------
# ID:            113
# Pack:          Pack 002 (101–200)
# Name:          Soul Code Invoker
# Class:         control
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Callable, Mapping, Any

def glyph_113(code: str, registry: Mapping[str, Callable[..., Any]], *args, **kwargs) -> Any:
    """
    Soul Code Invoker — deterministic dispatch into a safe registry.

    Overview
    --------
    Looks up `code` in `registry` and invokes it with given args/kwargs.

    Parameters
    ----------
    code : str
    registry : Mapping[str, Callable[..., Any]]

    Returns
    -------
    Any
        Result of the call.

    Examples
    --------
    >>> glyph_113("len", {"len": len}, [1,2,3])
    3

    Exceptions
    ----------
    - KeyError : unknown code.

    Complexity
    ----------
    - Time  : O(1) + cost(fn)
    - Space : O(1)
    """
    if code not in registry:
        raise KeyError(f"Unknown code '{code}'")
    return registry[code](*args, **kwargs)
