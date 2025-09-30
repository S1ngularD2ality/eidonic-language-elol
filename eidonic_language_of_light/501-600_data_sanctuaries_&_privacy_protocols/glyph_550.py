# glyph_550.py — Safe Transmit
# -----------------------------------------------------------------------------
# ID:            550
# Pack:          Pack 006 (501–600)
# Name:          Safe Transmit
# Class:         container
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib
from typing import Dict, Any

def glyph_550(payload: bytes, *, route: str = "local", key: bytes | None = None) -> Dict[str, Any]:
    """
    Safe Transmit — wrap bytes in a checksumed, intent-tagged envelope (no I/O).

    Overview
    --------
    Produces a deterministic **transmit plan** containing route, size, checksum,
    and optional HMAC for integrity. It **does not** perform network I/O.

    Parameters
    ----------
    payload : bytes
        Data to transmit.
    route : str, optional (default: ``"local"``)
        Logical route tag (e.g., "guardian://ingest").
    key : bytes | None, optional (default: ``None``)
        If provided, compute `hmac = HMAC_SHA256(key, payload)`.

    Returns
    -------
    Dict[str, Any]
        Envelope dict.

    Examples
    --------
    >>> plan = glyph_550(b"hello", route="guardian://ingest")
    >>> plan["size"], len(plan["sha256"]) == (5, True)
    True
    """
    env: Dict[str, Any] = {
        "type": "TransmitPlan",
        "route": route,
        "size": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }
    if key is not None:
        import hmac
        env["hmac"] = hmac.new(key, payload, hashlib.sha256).hexdigest()
    return env
