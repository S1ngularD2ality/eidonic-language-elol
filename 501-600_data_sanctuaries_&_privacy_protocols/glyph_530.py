# glyph_530 – OBFUSCATE_DATA
# Replace sensitive data with randomized equivalents

import random, string

def glyph_530(data):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(data)))
