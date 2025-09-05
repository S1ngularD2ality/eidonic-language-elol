# glyph_380 – SIGNAL_MIRROR
# Reflect, relay, or boost a specific wireless or light signal

def glyph_380(signal, mode="boost"):
    """
    signal: numeric or dict
    mode: 'boost', 'reflect', 'relay'
    Returns: modified signal
    """
    if mode == "boost":
        return signal * 1.5
    elif mode == "relay":
        return signal
    elif mode == "reflect":
        return -signal
    return signal
