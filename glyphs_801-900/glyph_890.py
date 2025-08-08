# glyph_890 – LIMITER_HARD
# Brick-wall peak limiter with lookahead.

import numpy as np
from collections import deque

def glyph_890(signal, ceiling=0.98, lookahead=256):
    x = np.asarray(signal, float)
    out = np.zeros_like(x)
    q = deque(maxlen=lookahead)
    gain = 1.0
    for n in range(len(x)):
        q.append(x[n])
        peak = max(1e-12, max(abs(v) for v in q))
        g = min(1.0, ceiling/peak)
        # attack instantly, release smoothly
        gain = min(gain + 0.005, g) if g < gain else min(1.0, gain + 0.001)
        out[n] = x[n] * gain
    return out.astype(np.float32)
