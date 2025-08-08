# glyph_625 – PET_AWARE_MODE
# Adjust motion to avoid startling or harming pets

def glyph_625(pet_detected):
    return 'soft_slow' if pet_detected else 'normal'
