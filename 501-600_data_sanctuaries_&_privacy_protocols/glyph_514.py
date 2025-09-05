# glyph_514 – PRIVACY_MODE
# Redact sensitive keywords in a text block

def glyph_514(text, keywords):
    for word in keywords:
        text = text.replace(word, "[REDACTED]")
    return text
