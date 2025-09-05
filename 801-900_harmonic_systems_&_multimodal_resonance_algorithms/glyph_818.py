# glyph_818 – QUANTUM_CROP_CIRCLE_ENCODER
# Encode message into a compact binary glyph stream.

def glyph_818(message: str) -> str:
    """
    Returns bitstring of message bytes, concatenated.
    """
    return ''.join(f"{ord(c):08b}" for c in message)
