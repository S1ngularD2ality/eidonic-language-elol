# glyph_422 – INSTANT_SIGNAL
# Send urgent, high-priority signal across all channels instantly

def glyph_422(channels, message):
    """
    channels: list of channel names/objects
    message: string
    Returns: dict of channel:delivered_message
    """
    return {ch: message for ch in channels}
