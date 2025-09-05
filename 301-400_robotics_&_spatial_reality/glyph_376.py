# glyph_376 – NOISE_FILTER
# Filter out background noise for clear audio input or comms

def glyph_376(audio_data, noise_floor=0.1):
    """
    audio_data: list of floats
    Returns: list of filtered audio points
    """
    return [x for x in audio_data if abs(x) > noise_floor]
