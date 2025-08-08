# glyph_781 – EVENT_HORIZON_MONITOR
# Watches for events that mark irreversible state changes.

def glyph_781(events):
    return [e for e in events if e.get("irreversible", False)]
