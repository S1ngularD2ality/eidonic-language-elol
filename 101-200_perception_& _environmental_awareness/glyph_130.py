def glyph_130(arc_stream):
    """
    💠 Calculates moving average with window size 3.
    Used in temporal smoothing of arc pathways.
    """
    return [(arc_stream[i] + arc_stream[i+1] + arc_stream[i+2]) / 3 for i in range(len(arc_stream)-2)]
