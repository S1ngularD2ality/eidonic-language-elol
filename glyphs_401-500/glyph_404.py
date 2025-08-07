# glyph_404 – MULTIMODAL_LINK
# Create real-time data bridges between text, vision, speech, and motion

def glyph_404(input_data):
    """
    input_data: dict of 'text', 'vision', 'speech', 'motion'
    Returns: linked_data (merged or indexed)
    """
    linked_data = {}
    for k, v in input_data.items():
        linked_data[k] = v
    return linked_data
