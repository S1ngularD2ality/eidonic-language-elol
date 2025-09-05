# glyph_895 – GRANULAR_STRETCH
# Basic granular time-stretching with windowed overlap-add.

import numpy as np

def glyph_895(signal, sr, stretch=1.5, grain_ms=50, hop_ratio=0.5):
    x = np.asarray(signal, float)
    grain = max(32, int(sr*grain_ms/1000))
    hop_in  = max(1, int(grain*hop_ratio))
    hop_out = max(1, int(hop_in*stretch))
    win = np.hanning(grain)
    frames=[]
    for i in range(0, len(x)-grain+1, hop_in):
        frames.append(x[i:i+grain]*win)
    out_len = (len(frames)-1)*hop_out + grain
    y = np.zeros(out_len)
    w = np.zeros(out_len)
    for k, fr in enumerate(frames):
        i = k*hop_out
        y[i:i+grain] += fr
        w[i:i+grain] += win
    w[w==0]=1.0
    return (y/w).astype(np.float32)
