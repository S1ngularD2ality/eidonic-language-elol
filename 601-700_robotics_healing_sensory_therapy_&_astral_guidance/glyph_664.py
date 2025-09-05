# glyph_664 – BOT_TO_BOT_SIGNAL
# Communicate status to nearby bots

def glyph_664(status, bots_in_range):
    return {bot: status for bot in bots_in_range}
