# glyph_449 – SYNTHESIS_NODE
# Create a node to synthesize information from multiple sources

def glyph_449(*sources):
    """
    sources: any number of data inputs
    Returns: synthesized string
    """
    return " | ".join(map(str, sources))
