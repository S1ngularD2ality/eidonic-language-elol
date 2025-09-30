# glyph_515.py — Secure Backup
# -----------------------------------------------------------------------------
# ID:            515
# Pack:          Pack 006 (501–600)
# Name:          Secure Backup
# Class:         crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True  # envelope only; no filesystem
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_515(snapshot: Mapping[str, Any], *, key: bytes, nonce: bytes) -> Dict[str, Any]:
    """
    Secure Backup — seal a JSON-serializable snapshot (logical backup).

    Overview
    --------
    Serializes canonically and applies `Data Seal`. Returns envelope + checksum.

    Parameters
    ----------
    snapshot : Mapping[str,Any]
    key      : bytes
    nonce    : bytes

    Returns
    -------
    Dict[str,Any] : {'sealed': {...}, 'checksum': str}

    Examples
    --------
    >>> env = glyph_515({'a':1}, key=b'k', nonce=b'n')
    >>> isinstance(env['checksum'], str) and len(env['checksum']) == 64
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    import json
    raw = json.dumps(dict(snapshot), sort_keys=True, separators=(",", ":")).encode()
    sealed = glyph_501(raw, key=key, nonce=nonce)  # type: ignore
    return {"sealed": sealed, "checksum": hashlib.sha256(raw).hexdigest()}
