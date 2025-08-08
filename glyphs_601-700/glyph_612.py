# glyph_612 – EMERGENCY_YIELD
# Immediately stop and yield if a human is in danger zone

def glyph_612(proximity_alert):
    return 'STOP' if proximity_alert else 'CONTINUE'
