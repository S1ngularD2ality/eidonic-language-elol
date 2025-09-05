# glyph_379 – LOUD_SOUND_ALERT
# Detect and respond to sudden loud noises

def glyph_379(mic_data, loudness_threshold=80):
    """
    mic_data: list of volume levels (dB)
    Returns: True if loud event detected
    """
    return any(v > loudness_threshold for v in mic_data)
