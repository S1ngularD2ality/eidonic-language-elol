# glyph_866 – CEPSTRUM_PITCH
# Estimate fundamental via cepstrum peak in voiced range.

import numpy as np

def glyph_866(frame, sr, fmin=60, fmax=400):
    """
    frame: 1D signal window
    returns (f0_hz or 0.0)
    """
    x = np.asarray(frame, float)
    X = np.fft.rfft(x*np.hanning(len(x)))
    logmag = np.log(np.abs(X) + 1e-12)
    c = np.fft.irfft(logmag)
    qmin = int(sr/fmax); qmax = int(sr/fmin)
    qrange = c[qmin:qmax]
    if len(qrange) == 0:
        return 0.0
    q = np.argmax(qrange) + qmin
    return float(sr / q)
