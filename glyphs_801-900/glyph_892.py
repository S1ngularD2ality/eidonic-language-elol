# glyph_892 – NOISE_GATE
# Simple downward expander / gate using envelope follower.

def glyph_892(signal, threshold=0.02, ratio=2.0, attack=0.01, release=0.1):
    env = 0.0
    out = []
    for s in signal:
        a = abs(float(s))
        coeff = attack if a > env else release
        env = (1 - coeff)*env + coeff*a
        if env < threshold:
            g = (env/threshold)**(ratio - 1.0)
        else:
            g = 1.0
        out.append(float(s)*g)
    return out
