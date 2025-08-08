# glyph_561 – DUAL_LAYER_HASH
# Hash data twice with different algorithms for extra security

import hashlib

def glyph_561(data):
    first = hashlib.sha256(data.encode()).hexdigest()
    second = hashlib.sha512(first.encode()).hexdigest()
    return second
