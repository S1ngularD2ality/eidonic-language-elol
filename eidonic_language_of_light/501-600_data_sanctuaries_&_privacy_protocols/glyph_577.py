# glyph_577.py — File Integrity Check
# -----------------------------------------------------------------------------
# ID:            577
# Pack:          Pack 006 (501–600)
# Name:          File Integrity Check
# Class:         hashing_fingerprints
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure hashing; no FS I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib
from typing import Dict

def glyph_577(files: Dict[str, bytes]) -> Dict[str, str]:
    """
    File Integrity Check — compute SHA-256 for each filename→bytes.

    Returns
    -------
    Dict[str,str] : filename → sha256_hex

    Examples
    --------
    >>> glyph_577({'a':b'x'})['a']
    '2d711642b726b04401627ca9fbac32f5da7e5c...'[:10]  # starts with
    """
    return {name: hashlib.sha256(data).hexdigest() for name, data in sorted(files.items())}
