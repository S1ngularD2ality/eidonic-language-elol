# glyph_862 – KEY_ESTIMATE_FROM_CHROMA
# Estimate musical key using Krumhansl-like templates (major/minor).

import numpy as np

_TEMPL_MAJOR = np.array([6.35,2.23,3.48,2.33,4.38,4.09,2.52,5.19,2.39,3.66,2.29,2.88])
_TEMPL_MINOR = np.array([6.33,2.68,3.52,5.38,2.60,3.53,2.54,4.75,3.98,2.69,3.34,3.17])

def glyph_862(chroma):
    """
    chroma: [frames,12] or [12]
    Returns: (key_name, mode, score)
    """
    C = np.asarray(chroma, dtype=float)
    if C.ndim == 2:
        C = C.mean(axis=0)
    C = C / (np.linalg.norm(C) + 1e-12)
    best = ("C", "major", -1.0)
    pcs = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    for rot in range(12):
        maj = np.roll(_TEMPL_MAJOR, rot); maj /= np.linalg.norm(maj)
        minr= np.roll(_TEMPL_MINOR, rot); minr/= np.linalg.norm(minr)
        sM = float(np.dot(C, maj)); sN = float(np.dot(C, minr))
        if sM > best[2]:
            best = (pcs[rot], "major", sM)
        if sN > best[2]:
            best = (pcs[rot], "minor", sN)
    return best
