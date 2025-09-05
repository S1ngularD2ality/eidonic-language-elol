# glyph_324 – SOUND_MAP
# Build a spatial sound map using microphone arrays for 3D awareness

def glyph_324(mic_data):
    """
    mic_data: dict of mic_id:(volume, position)
    Returns: sound_intensity_map
    """
    sound_map = {}
    for mic_id, (volume, position) in mic_data.items():
        sound_map[position] = volume
    return sound_map
