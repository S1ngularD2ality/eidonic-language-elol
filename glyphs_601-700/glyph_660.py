# glyph_660 – COMPASS_SAFE_NAV
# Navigate using compass bearing for safety in open areas

def glyph_660(current_heading, target_heading):
    return (target_heading - current_heading) % 360
