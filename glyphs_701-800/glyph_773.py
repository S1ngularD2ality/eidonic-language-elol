# glyph_773 – IMMUNE_SYSTEM_SIMULATION
# AI immune system simulation for anomaly defense.

def glyph_773(signals):
    return [s for s in signals if not looks_like_threat(s)]

def looks_like_threat(signal):
    return "malicious" in signal.lower()
