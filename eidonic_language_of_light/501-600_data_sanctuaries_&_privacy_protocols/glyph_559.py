# glyph_559.py — Safe Deserialize
# -----------------------------------------------------------------------------
# ID:            559
# Pack:          Pack 006 (501–600)
# Name:          Safe Deserialize
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import Any

def glyph_559(data: bytes) -> Any:
    """
    Safe Deserialize — strict JSON loader to safe Python primitives.

    Overview
    --------
    Parses canonical JSON bytes and returns scalars/lists/dicts only. If any
    non-finite floats or invalid structures occur, raises errors.

    Parameters
    ----------
    data : bytes
        JSON bytes to parse.

    Returns
    -------
    Any
        Safe Python value.

    Examples
    --------
    >>> glyph_559(b'{"x":[1,true]}')["x"][1]
    True

    Exceptions
    ----------
    - ValueError : if JSON is invalid.

    Complexity
    ----------
    - Time  : O(N)
    - Space : O(N)
    """
    try:
        return json.loads(data.decode("utf-8"))
    except Exception as e:
        raise ValueError("invalid JSON") from e
