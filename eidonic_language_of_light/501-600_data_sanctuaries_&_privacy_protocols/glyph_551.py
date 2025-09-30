# glyph_551.py — Sandbox Exec
# -----------------------------------------------------------------------------
# ID:            551
# Pack:          Pack 006 (501–600)
# Name:          Sandbox Exec
# Class:         gate
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import ast
from typing import Any, Dict

def glyph_551(expr: str, *, unsafe_exec: bool = False) -> Dict[str, Any]:
    """
    Sandbox Exec — **refuses** arbitrary exec; permits safe literal evaluation only.

    Overview
    --------
    To honor Guardian/Mirror safety, this glyph **does not** execute code. If
    `unsafe_exec=False`, it parses the expression and returns `ast.literal_eval(expr)`
    results for literals/tuples/lists/dicts. If `unsafe_exec=True`, it still refuses
    and explains mitigation.

    Parameters
    ----------
    expr : str
        Expression to parse.
    unsafe_exec : bool, optional (default: ``False``)
        Even when True, this glyph declines execution.

    Returns
    -------
    Dict[str, Any]
        {"status":"ok","result":...} or {"status":"refused","reason":...}

    Examples
    --------
    >>> glyph_551("[1,2,3]")["result"] == [1,2,3]
    True
    """
    try:
        node = ast.parse(expr, mode="eval")
        result = ast.literal_eval(node)
        return {"status": "ok", "result": result}
    except Exception as e:
        # Even if unsafe_exec=True, never run arbitrary code
        return {"status": "refused", "reason": f"execution denied: {e}"}
