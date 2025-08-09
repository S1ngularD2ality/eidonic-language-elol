# glyph_944 – TRAFFIC_PADDING_SCHED
"""
Traffic Padding Scheduler

Transforms bursty traffic into nearly constant-rate frames to resist traffic analysis.
Fills silence with chaff frames; trims or batches large packets.

APIs:
- frame_outgoing(pkts: List[bytes], frame_size=512, rate_hz=50) -> List[bytes]
"""

import os
from typing import List

def frame_outgoing(pkts: List[bytes], frame_size: int = 512, rate_hz: int = 50) -> List[bytes]:
    out = []
    for p in pkts:
        # split into fixed frames; pad tail
        for i in range(0, len(p), frame_size):
            block = p[i:i+frame_size]
            if len(block) < frame_size:
                block = block + os.urandom(frame_size - len(block))
            out.append(block)
    # Caller should emit at rate_hz; here we just return framed blocks
    if not out:
        out.append(os.urandom(frame_size))
    return out
