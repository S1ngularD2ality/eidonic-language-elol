def glyph_114(flow_nodes):
    """
    💠 Filters flow nodes exceeding the harmonic average.
    Mirrors the concept of ‘ascendant resonance’ filters.
    """
    threshold = sum(flow_nodes) / len(flow_nodes)
    return [n for n in flow_nodes if n > threshold]
