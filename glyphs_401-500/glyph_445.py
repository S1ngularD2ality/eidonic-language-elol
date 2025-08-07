# glyph_445 – MODALITY_CHAIN
# Link multiple modalities in a sequence for complex interaction

def glyph_445(modality_sequence, data):
    """
    modality_sequence: list of modality names
    data: any
    Returns: processed sequence (simulated)
    """
    for m in modality_sequence:
        data = f"{m}({data})"
    return data
