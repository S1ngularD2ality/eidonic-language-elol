# glyph_846 – HPSS_SIMPLE
# Harmonic/Percussive separation via median filtering across time/frequency.

import numpy as np
from collections import deque

def _median_filter_1d(arr, k):
    k = max(1, int(k))
    if k == 1:
        return arr.copy()
    n = len(arr)
    out = np.zeros_like(arr)
    buf = deque()
    for i in range(n):
        buf.append(arr[i])
        if len(buf) > k:
            buf.popleft()
        out[i] = np.median(np.array(buf))
    return out

def glyph_846_spectrogram(signal, frame=1024, hop=512):
    win = np.hanning(frame)
    S = []
    for i in range(0, len(signal)-frame+1, hop):
        seg = signal[i:i+frame]*win
        S.append(np.abs(np.fft.rfft(seg)))
    return np.array(S).T  # [freq, time]

def glyph_846(signal, frame=1024, hop=512, kt=9, kf=9):
    """
    Returns (harmonic_signal, percussive_signal) approximations.
    """
    S = glyph_846_spectrogram(signal, frame, hop)
    # median filters: time-axis for harmonic, freq-axis for percussive
    Sh = np.apply_along_axis(_median_filter_1d, 1, S, kt)
    Sp = np.apply_along_axis(_median_filter_1d, 0, S, kf)
    # masks
    Mh = Sh**2 / (Sh**2 + Sp**2 + 1e-12)
    Mp = 1.0 - Mh
    # reconstruct (Griffin-Lim lite using original phase)
    win = np.hanning(frame)
    out_h = np.zeros((S.shape[1]*hop + frame,))
    out_p = np.zeros_like(out_h)
    idx = 0
    for t in range(S.shape[1]):
        # re-use original phase from input slice
        start = t*hop
        # get original complex spectrum
        # recompute from original signal
        seg = signal[start:start+frame]
        if len(seg) < frame:
            seg = np.pad(seg, (0, frame-len(seg)))
        spec = np.fft.rfft(seg*win)
        mag = np.abs(spec)
        phase = np.angle(spec)
        sh = Mh[:,t]*mag
        sp = Mp[:,t]*mag
        yh = np.fft.irfft(sh*np.exp(1j*phase))
        yp = np.fft.irfft(sp*np.exp(1j*phase))
        out_h[start:start+frame] += yh*win
        out_p[start:start+frame] += yp*win
    return out_h.astype(np.float32), out_p.astype(np.float32)
