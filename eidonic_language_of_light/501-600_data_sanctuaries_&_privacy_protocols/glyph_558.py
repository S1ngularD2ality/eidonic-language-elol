# glyph_558.py — Safe Serialize
# -----------------------------------------------------------------------------
# ID:            558
# Pack:          Pack 006 (501–600)
# Name:          Safe Serialize
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

_ALLOWED_SCALARS = (str, int, float, bool, type(None))

def _validate(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {str(k): _validate(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_validate(v) for v in obj]
    if isinstance(obj, _ALLOWED_SCALARS):
        return obj
    raise TypeError(f"unsupported type: {type(obj).__name__}")

def glyph_558(obj: Any) -> bytes:
    """
    Safe Serialize — JSON-canonical serializer that rejects unsafe types.

    Overview
    --------
    Validates a structure (scalars, lists, dicts) and emits UTF-8 JSON with
    sorted keys and compact separators. This replaces unsafe pickle usage.

    Parameters
    ----------
    obj : Any
        Value to serialize (must be composed of safe types).

    Returns
    -------
    bytes
        Canonical JSON bytes.

    Examples
    --------
    >>> glyph_558({"b":1,"a":[True, None]})
    b'{"a":[true,null],"b":1}'
    """
    safe = _validate(obj)
    return json.dumps(safe, sort_keys=True, separators=(",", ":")).encode("utf-8")
