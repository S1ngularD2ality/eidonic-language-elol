# glyph_541.py — Secure Archive
# -----------------------------------------------------------------------------
# ID:            541
# Pack:          Pack 006 (501–600)
# Name:          Secure Archive
# Class:         container
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from __future__ import annotations
from typing import Dict, Tuple
import base64, json, hashlib, zlib, hmac

def glyph_541(files: Dict[str, bytes], *, key: bytes | None = None) -> Tuple[bytes, str]:
    """
    Secure Archive — produce a compressed, integrity-checked envelope for multiple files.

    Overview
    --------
    Accepts a mapping of filenames → bytes and emits a **single archive blob** plus a
    SHA-256 manifest. The envelope is a JSON header (file sizes, hashes) + binary body,
    compressed via DEFLATE. If `key` is provided, an HMAC-SHA256 **MAC** is appended
    to the header for tamper evidence (deterministic given inputs).

    Parameters
    ----------
    files : Dict[str, bytes]
        Filenames to include and their byte contents.
    key : bytes | None, optional (default: ``None``)
        If provided, compute `mac = HMAC_SHA256(key, header_bytes)` and embed it.

    Returns
    -------
    (bytes, str)
        Tuple of (archive_blob, manifest_sha256_hex).

    Examples
    --------
    >>> blob, manifest = glyph_541({"a.txt": b"hi", "b.bin": b"\\x00\\x01"})
    >>> isinstance(blob, (bytes, bytearray)) and len(manifest) == 64
    True

    Exceptions
    ----------
    - ValueError : if duplicate or empty filenames are provided.

    Complexity
    ----------
    - Time  : O(N) over total input size
    - Space : O(N) for the compressed envelope
    """
    if any((not name) or ("\x00" in name) for name in files.keys()):
        raise ValueError("filenames must be non-empty and free of NUL")
    # header with per-file hashes
    header = {
        "format": "ELoL.SecureArchive.v1",
        "files": [
            {
                "name": name,
                "size": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "b64": base64.b64encode(data).decode("ascii"),
            }
            for name, data in sorted(files.items())
        ],
    }
    header_bytes = json.dumps(header, separators=(",", ":"), sort_keys=True).encode("utf-8")
    if key is not None:
        mac = hmac.new(key, header_bytes, hashlib.sha256).hexdigest()
        header["mac"] = mac
        header_bytes = json.dumps(header, separators=(",", ":"), sort_keys=True).encode("utf-8")
    # compress header (text) to blob
    blob = zlib.compress(header_bytes, level=9)
    manifest = hashlib.sha256(header_bytes).hexdigest()
    return blob, manifest
