# glyph_536.py — Key Rotate
# -----------------------------------------------------------------------------
# ID:            536
# Pack:          Pack 006 (501–600)
# Name:          Key Rotate
# Class:         key_management
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # HMAC-based KDF step
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hmac, hashlib

def glyph_536(old_key: bytes, *, label: bytes, counter: int) -> bytes:
    """
    Key Rotate — derive a next-generation key from an old key + label + counter.

    Overview
    --------
    Returns HMAC(old_key, label||counter_be). Deterministic, stateless KDF step.

    Parameters
    ----------
    old_key : bytes
    label   : bytes
    counter : int

    Returns
    -------
    bytes : 32-byte key

    Examples
    --------
    >>> isinstance(glyph_536(b'k', label=b'app', counter=1), bytes)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return hmac.new(old_key, label + counter.to_bytes(8, "big"), hashlib.sha256).digest()
