# glyph_958 – PADDED_CHANNEL_FRAMER
"""
Padded Channel Framer (Constant-Rate I/O)

Encapsulates payloads into fixed-size frames with length headers and padding.
Defends against size and timing side-channels when combined with uniform pacing.

APIs:
- frame(payload: bytes, frame_size=1024) -> bytes
- deframe(stream: bytes, frame_size=1024) -> List[bytes]
"""

import os
from typing import List

def frame(payload: bytes, frame_size: int = 1024) -> bytes:
    assert frame_size >= 16
    header = len(payload).to_bytes(4,"big")
    pad_len = frame_size - 4 - len(payload)
    if pad_len < 0:
        # split externally; here we require single-frame
        raise ValueError("payload too large for single frame")
    return header + payload + os.urandom(pad_len)

def deframe(stream: bytes, frame_size: int = 1024) -> List[bytes]:
    assert len(stream) % frame_size == 0
    out=[]
    for i in range(0, len(stream), frame_size):
        frame_bytes = stream[i:i+frame_size]
        L = int.from_bytes(frame_bytes[:4],"big")
        out.append(frame_bytes[4:4+L])
    return out
