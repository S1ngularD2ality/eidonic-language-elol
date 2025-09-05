# glyph_538 – STEALTH_MODE
# Hide system presence from basic network scans

def glyph_538(status):
    return "offline" if status == "stealth" else "online"
