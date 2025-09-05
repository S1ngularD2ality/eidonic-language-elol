# glyph_387 – PANIC_MODE
# Enter emergency shutdown or rapid escape routine

def glyph_387(trigger):
    """
    trigger: bool
    Returns: 'shutdown' or 'escape' or None
    """
    return "shutdown" if trigger == "shutdown" else "escape" if trigger else None
