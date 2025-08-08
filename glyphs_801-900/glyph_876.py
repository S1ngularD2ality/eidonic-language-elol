# glyph_876 – QUATERNION_UTILS
# Normalize, multiply, and rotate a 3D vector using quaternions.

import numpy as np

def glyph_876_normalize(q):
    q = np.asarray(q, float)
    return q / (np.linalg.norm(q) + 1e-12)

def glyph_876_mul(q1, q2):
    w1,x1,y1,z1 = q1; w2,x2,y2,z2 = q2
    return np.array([
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2
    ])

def glyph_876_rotate(q, v):
    q = glyph_876_normalize(np.asarray(q))
    vq = np.array([0.0, *v])
    qi = np.array([q[0], -q[1], -q[2], -q[3]])
    r = glyph_876_mul(glyph_876_mul(q, vq), qi)
    return r[1:]
