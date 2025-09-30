# glyph_566.py — Secure Session Store
# -----------------------------------------------------------------------------
# ID:            566
# Pack:          Pack 006 (501–600)
# Name:          Secure Session Store
# Class:         session_security
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # canonical JSON + seal; no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib
from typing import Mapping, Any, Dict

def glyph_566(session: Mapping[str, Any], *, key: bytes, nonce: bytes) -> Dict[str, Any]:
    """
    Secure Session Store — seal a session dict (no tokens).

    Overview
    --------
    Canonicalize the mapping and seal bytes with `Data Seal`.

    Parameters
    ----------
    session : Mapping[str,Any]
    key     : bytes
    nonce   : bytes

    Returns
    -------
    Dict[str,Any] : {'sealed': {...}, 'checksum': str}

    Examples
    --------
    >>> env = glyph_566({'user':'a','exp':10}, key=b'k', nonce=b'n'); 'sealed' in env
    True
    """
    raw = json.dumps(dict(session), sort_keys=True, separators=(",", ":")).encode()
    return {"sealed": glyph_501(raw, key=key, nonce=nonce),  # type: ignore
            "checksum": hashlib.sha256(raw).hexdigest()}
