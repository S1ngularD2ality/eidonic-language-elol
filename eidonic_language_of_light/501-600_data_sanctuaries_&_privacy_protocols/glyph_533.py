# glyph_533.py — IP Encrypt
# -----------------------------------------------------------------------------
# ID:            533
# Pack:          Pack 006 (501–600)
# Name:          IP Encrypt
# Class:         privacy_transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # toy FPE-like; not reversible
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hmac, hashlib

def glyph_533(ip: str, *, key: bytes) -> str:
    """
    IP Encrypt — educational, format-preserving obfuscation for IPv4.

    Overview
    --------
    Maps each octet to a pseudo-random byte via HMAC(key, index||octet). One-way.

    Parameters
    ----------
    ip  : str
    key : bytes

    Returns
    -------
    str : obfuscated dotted quad, or '***' on invalid input.

    Examples
    --------
    >>> glyph_533('1.2.3.4', key=b'k').count('.') == 3
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    parts = ip.split(".")
    if len(parts) != 4:
        return "***"
    outs = []
    for i, p in enumerate(parts):
        try:
            v = int(p) & 0xFF
        except Exception:
            return "***"
        h = hmac.new(key, b"IP"+bytes([i, v]), hashlib.sha256).digest()
        outs.append(str(h[0]))
    return ".".join(outs)
