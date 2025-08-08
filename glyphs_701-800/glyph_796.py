# glyph_796 – MEMORY_FRAGMENT_CLEANER
# Cleans up unused memory fragments.

def glyph_796(memory_blocks):
    return [block for block in memory_blocks if block.get("active", False)]
