# glyph_367 – EMERGENCY_SIGNAL
# Emit emergency signals (sound, light, wireless) when in distress

def glyph_367(signal_type="sound"):
    """
    signal_type: 'sound', 'light', 'wireless'
    Returns: signal command
    """
    return f"emit {signal_type} emergency"
