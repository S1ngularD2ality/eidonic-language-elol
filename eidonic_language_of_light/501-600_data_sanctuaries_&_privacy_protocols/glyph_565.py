# glyph_565.py — Decrypt Zip
# -----------------------------------------------------------------------------
# ID:            565
# Pack:          Pack 006 (501–600)
# Name:          Decrypt Zip
# Class:         container_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # seal unwrap + inflate; no filesystem I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import zlib, json

def glyph_565(sealed: dict, *, key: bytes) -> dict:
    """
    Decrypt Zip — unseal and return the canonical header.

    Returns
    -------
    dict : header (fmt, files)

    Examples
    --------
    >>> hdr = glyph_565(glyph_564({'x':b'y'}, key=b'k', nonce=b'n')['sealed'], key=b'k')
    >>> hdr['fmt'] == 'ELoL.Zip.v1'
    True
    """
    blob = glyph_502(sealed, key=key)  # type: ignore
    raw = zlib.decompress(blob)
    return json.loads(raw.decode())
