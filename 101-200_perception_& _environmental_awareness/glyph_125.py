def glyph_125(signal_array):
    """
    💠 Filters out negative pulses.
    A basic protective filter for corrupted waveforms.
    """
    return [x for x in signal_array if x >= 0]
