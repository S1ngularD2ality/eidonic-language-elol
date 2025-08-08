# glyph_891 – ENVELOPE_FOLLOW
# Attack/Release envelope follower.

def glyph_891(signal, attack=0.01, release=0.1):
    env = 0.0
    out = []
    for s in signal:
        s = abs(float(s))
        coeff = attack if s > env else release
        env = (1 - coeff)*env + coeff*s
        out.append(env)
    return out
