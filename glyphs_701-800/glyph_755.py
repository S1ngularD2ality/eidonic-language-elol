# glyph_755 – EMERGENCY_SHUTDOWN
# Trigger an immediate, safe system halt.

import sys

def glyph_755(reason):
    print(f"Emergency shutdown triggered: {reason}")
    sys.exit(1)
