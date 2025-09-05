# glyph_929 – SIDECHANNEL_NOISE
"""
Side-Channel Noise Generator

Injects time/CPU noise during sensitive ops to blur timing/power patterns.
Use judiciously; adds overhead and is not a silver bullet.
"""

import time, os, random

def sc_noise(duration_ms: int = 3):
    end = time.perf_counter() + duration_ms/1000.0
    junk = 0
    while time.perf_counter() < end:
        junk ^= random.getrandbits(32)
        _ = os.urandom(1)
    return junk
