# glyph_386 – PERSONAL_ID
# Recognize known people or robots via visual, RFID, or audio signature

def glyph_386(id_signals, known_signatures):
    """
    id_signals: dict of type:value, known_signatures: set of signatures
    Returns: matched id or None
    """
    for sig in id_signals.values():
        if sig in known_signatures:
            return sig
    return None
