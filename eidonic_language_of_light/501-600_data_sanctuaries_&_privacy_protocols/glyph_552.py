# glyph_552.py — Secure Ping
# -----------------------------------------------------------------------------
# ID:            552
# Pack:          Pack 006 (501–600)
# Name:          Secure Ping
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib
from typing import Dict

def glyph_552(endpoint: str, *, nonce: bytes = b"") -> Dict[str, str | int]:
    """
    Secure Ping — simulate an authenticated reachability check (offline).

    Overview
    --------
    Generates a deterministic status “echo” by hashing `(endpoint || nonce)` and
    deriving a pseudo-latency (ms) from the digest. No network I/O occurs.

    Parameters
    ----------
    endpoint : str
        Target logical endpoint.
    nonce : bytes, optional (default: ``b""``)
        Optional salt to vary the echo.

    Returns
    -------
    Dict[str, str | int]
        {"endpoint":..., "status":"ok", "latency_ms":int, "echo":hex}

    Examples
    --------
    >>> glyph_552("guardian://node")["status"]
    'ok'
    """
    h = hashlib.sha256(endpoint.encode("utf-8") + nonce).hexdigest()
    latency = int(h[:4], 16) % 200  # 0..199 ms
    return {"endpoint": endpoint, "status": "ok", "latency_ms": latency, "echo": h}
