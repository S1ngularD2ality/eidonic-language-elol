# glyph_560.py — Shared Secret
# -----------------------------------------------------------------------------
# ID:            560
# Pack:          Pack 006 (501–600)
# Name:          Shared Secret
# Class:         combinator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib
from typing import Tuple

def glyph_560(part_a: bytes, part_b: bytes, *, label: bytes = b"ELoL-SharedSecret") -> Tuple[bytes, str]:
    """
    Shared Secret — derive a joint secret from two parts (deterministic KDF).

    Overview
    --------
    Computes `secret = SHA256(label || len(a) || a || len(b) || b)` and returns
    `(secret_bytes, hex)`. This is a **deterministic combiner** for offline tests,
    not a replacement for Diffie-Hellman.

    Parameters
    ----------
    part_a : bytes
        First secret contribution.
    part_b : bytes
        Second secret contribution.
    label : bytes, optional (default: ``b"ELoL-SharedSecret"``)
        Domain separation label.

    Returns
    -------
    (bytes, str)
        32-byte secret and its hex string.

    Examples
    --------
    >>> s, hx = glyph_560(b"a", b"b")
    >>> len(s) == 32 and len(hx) == 64
    True
    """
    enc_len_a = len(part_a).to_bytes(4, "big")
    enc_len_b = len(part_b).to_bytes(4, "big")
    material = label + enc_len_a + part_a + enc_len_b + part_b
    digest = hashlib.sha256(material).digest()
    return digest, digest.hex()
