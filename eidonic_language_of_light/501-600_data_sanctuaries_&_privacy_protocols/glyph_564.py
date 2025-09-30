# glyph_564.py — Encrypt Zip
# -----------------------------------------------------------------------------
# ID:            564
# Pack:          Pack 006 (501–600)
# Name:          Encrypt Zip
# Class:         container_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # zlib + seal; no filesystem I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import zlib, hashlib
from typing import Dict, Any

def glyph_564(files: Dict[str, bytes], *, key: bytes, nonce: bytes) -> Dict[str, Any]:
    """
    Encrypt Zip — compress a filename→bytes map and seal it.

    Overview
    --------
    Builds a canonical header then DEFLATE-compresses it; seals bytes using
    `Data Seal` semantics (glyph_501). No disk I/O.

    Parameters
    ----------
    files : Dict[str, bytes]
    key   : bytes
    nonce : bytes

    Returns
    -------
    Dict[str,Any] : {'sealed': {'nonce','ct','tag'}, 'size': int, 'sha256': str}

    Examples
    --------
    >>> out = glyph_564({'a.txt':b'hi'}, key=b'k', nonce=b'n'); 'sealed' in out
    True
    """
    import json
    hdr = {"fmt": "ELoL.Zip.v1", "files": sorted([(k, len(v), hashlib.sha256(v).hexdigest()) for k,v in files.items()])}
    raw = json.dumps(hdr, sort_keys=True, separators=(",", ":")).encode()
    blob = zlib.compress(raw, level=9)
    sealed = glyph_501(blob, key=key, nonce=nonce)  # type: ignore
    return {"sealed": sealed, "size": len(blob), "sha256": hashlib.sha256(blob).hexdigest()}
