# glyph_868 – STFT
# Short-time Fourier transform (complex) with Hann window.

import numpy as np

def glyph_868(signal, n_fft=1024, hop=256, center=True):
    x = np.asarray(signal, float)
    if center:
        pad = n_fft // 2
        x = np.pad(x, (pad, pad))
    win = np.hanning(n_fft)
    frames = []
    for i in range(0, len(x)-n_fft+1, hop):
        seg = x[i:i+n_fft] * win
        frames.append(np.fft.rfft(seg))
    return np.array(frames)  # [frames, n_fft//2+1] complex
