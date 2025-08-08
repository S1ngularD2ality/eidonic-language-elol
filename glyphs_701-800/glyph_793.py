# glyph_793 – SENTIMENT_ALIGNMENT_MONITOR
# Keeps system tone aligned to emotional target.

def glyph_793(messages, target="calm"):
    return all(target in m.lower() for m in messages)
