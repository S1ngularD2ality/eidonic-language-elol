# glyph_659 – HUMAN_APPROVAL_REQUIRED
# Pause action until human operator confirms

def glyph_659(is_approved):
    return 'execute' if is_approved else 'pause'
