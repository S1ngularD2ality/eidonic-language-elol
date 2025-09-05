# glyph_411 – MODALITY_MERGE
# Merge parallel input streams (audio, text, visual, haptic) into one workflow

def glyph_411(modalities):
    """
    modalities: dict of {type:data}
    Returns: merged structure (tuple of values)
    """
    return tuple(modalities.values())
