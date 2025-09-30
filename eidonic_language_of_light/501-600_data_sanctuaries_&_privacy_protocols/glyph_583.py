# glyph_583.py — Secure Video Stream
# -----------------------------------------------------------------------------
# ID:            583
# Pack:          Pack 006 (501–600)
# Name:          Secure Video Stream
# Class:         media_stream
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # chunked sealing; opaque bytes
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Dict, List

def glyph_583(frames: Sequence[bytes], *, key: bytes, nonce: bytes) -> Dict[str, List[bytes]]:
    """
    Secure Video Stream — seal a sequence of opaque video frames.

    Overview
    --------
    Applies `Data Seal` per frame with rolling nonce suffix.

    Parameters
    ----------
    frames : Sequence[bytes]
    key    : bytes
    nonce  : bytes

    Returns
    -------
    Dict[str,List[bytes]] : {'ct_frames': [...], 'tags': [...], 'nonce_base': bytes}

    Examples
    --------
    >>> out = glyph_583([b'F1', b'F2'], key=b'k', nonce=b'n'); len(out['ct_frames'])
    2
    """
    cts: List[bytes] = []
    tags: List[bytes] = []
    for i, fr in enumerate(frames):
        sealed = glyph_501(fr, key=key, nonce=nonce + i.to_bytes(4, "big"))  # type: ignore
        cts.append(sealed["ct"]); tags.append(sealed["tag"])
    return {"ct_frames": cts, "tags": tags, "nonce_base": nonce}
