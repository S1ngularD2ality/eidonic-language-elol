# glyph_855 – EQUAL_TEMPERAMENT_MAP
# Map MIDI note numbers to frequencies (A4=440 by default).

def glyph_855(midi_notes, a4=440.0):
    """
    midi_notes: iterable of ints
    returns list[float] frequencies
    """
    out=[]
    for n in midi_notes:
        f = a4 * (2 ** ((n - 69)/12))
        out.append(f)
    return out
