# glyph_847 – CHORD_FROM_PCP
# Infer chord label from pitch-class profile using cosine similarity.

import numpy as np

_CHORDS = {
    "C:maj":  [1,0,1,0,1,1,0,1,0,1,0,1],
    "C:min":  [1,0,1,1,0,1,0,1,1,0,1,0],
    "C#:maj":[0,1,0,1,0,1,1,0,1,0,1,0],
    "D:maj": [0,0,1,0,1,0,1,1,0,1,0,1],
    "D:min": [0,0,1,1,0,1,0,1,1,0,1,0],
    "E:maj": [1,0,0,1,0,1,0,1,1,0,1,0],  # enharmonics simplified
    "E:min": [1,0,0,1,1,0,1,0,1,1,0,1],
    "F:maj": [1,1,0,0,1,0,1,0,1,1,0,1],
    "G:maj": [1,0,1,0,1,0,1,1,0,1,1,0],
    "A:min": [1,0,1,1,0,1,0,1,1,0,1,0],
    "A:maj": [1,0,1,0,1,1,0,1,0,1,1,0],
    "B:min": [0,1,0,1,1,0,1,0,1,1,0,1],
}

def glyph_847(pcp):
    """
    pcp: length-12 pitch-class profile (list/np.array)
    returns (label, score)
    """
    v = np.asarray(pcp, dtype=float)
    if v.shape[0] != 12:
        raise ValueError("PCP must have 12 elements.")
    v = v / (np.linalg.norm(v) + 1e-12)
    best = None; best_score = -1.0
    for name, templ in _CHORDS.items():
        t = np.asarray(templ, dtype=float)
        t = t / (np.linalg.norm(t) + 1e-12)
        score = float(np.dot(v, t))
        if score > best_score:
            best_score, best = score, name
    return best, best_score
