# glyph_877 – SLERP
# Spherical linear interpolation between two quaternions.

import numpy as np

def glyph_877(q0, q1, t):
    q0 = np.asarray(q0, float); q1 = np.asarray(q1, float)
    q0 = q0/ (np.linalg.norm(q0)+1e-12)
    q1 = q1/ (np.linalg.norm(q1)+1e-12)
    dot = np.clip(np.dot(q0, q1), -1.0, 1.0)
    if dot < 0.0:
        q1 = -q1; dot = -dot
    if dot > 0.9995:
        return (q0 + t*(q1 - q0)) / (np.linalg.norm(q0 + t*(q1-q0))+1e-12)
    theta0 = np.arccos(dot)
    theta = theta0 * t
    q2 = (q1 - q0*dot) / (np.linalg.norm(q1 - q0*dot)+1e-12)
    return q0*np.cos(theta) + q2*np.sin(theta)
