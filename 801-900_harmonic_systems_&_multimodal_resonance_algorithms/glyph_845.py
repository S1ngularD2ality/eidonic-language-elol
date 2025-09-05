# glyph_845 – PHASE_VOCODER_TIME_STRETCH
# Basic phase vocoder for time-stretching (no pitch change).

import numpy as np

def glyph_845(signal, sr, stretch=1.5, frame=1024, hop=256):
    """
    stretch > 1 -> longer; < 1 -> shorter. Returns stretched signal (float32).
    """
    x = np.asarray(signal, dtype=float)
    win = np.hanning(frame)
    # analysis
    X = []
    phases = None
    for i in range(0, len(x)-frame+1, hop):
        seg = x[i:i+frame]*win
        spec = np.fft.rfft(seg)
        if phases is None:
            phases = np.angle(spec)
        X.append(np.vstack([np.abs(spec), np.angle(spec)]))
    X = np.stack(X, axis=2)  # [mag, phase, frame_idx]
    mag = X[0]; phase = X[1]
    # phase advance
    omega = np.linspace(0, np.pi, mag.shape[0])
    y_frames = int(mag.shape[1]*stretch)
    out = np.zeros(y_frames*hop + frame)
    last_phase = phase[:,0].copy()
    phase_adv = omega * hop
    pos = 0.0
    for t in range(y_frames):
        i = int(pos)
        frac = pos - i
        if i+1 >= mag.shape[1]:
            break
        # mag interpolation
        m = (1-frac)*mag[:,i] + frac*mag[:,i+1]
        # phase propagation
        dphi = (phase[:,i+1] - phase[:,i]) - phase_adv
        dphi = (dphi + np.pi) % (2*np.pi) - np.pi
        ph = last_phase + phase_adv + dphi
        last_phase = ph
        spec = m * np.exp(1j*ph)
        frame_sig = np.fft.irfft(spec) * win
        start = t*hop
        out[start:start+frame] += frame_sig
        pos += 1.0/stretch
    return out.astype(np.float32)
