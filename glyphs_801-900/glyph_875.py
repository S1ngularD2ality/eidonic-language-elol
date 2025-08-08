# glyph_875 – VITERBI_HMM
# Viterbi decoding for discrete HMM with log probabilities.

import numpy as np

def glyph_875(log_start, log_trans, log_emit, observations):
    """
    log_*: np arrays in log-space
    observations: list[int] emission indices
    Returns most likely state path (list[int])
    """
    S = len(log_start); T = len(observations)
    V = np.full((S, T), -np.inf)
    B = np.full((S, T), -1, dtype=int)
    V[:,0] = log_start + log_emit[:, observations[0]]
    for t in range(1, T):
        for s in range(S):
            scores = V[:, t-1] + log_trans[:, s]
            b = int(np.argmax(scores))
            V[s, t] = scores[b] + log_emit[s, observations[t]]
            B[s, t] = b
    path = [int(np.argmax(V[:, -1]))]
    for t in range(T-1, 0, -1):
        path.append(int(B[path[-1], t]))
    path.reverse()
    return path
