# glyph_636 – LOW_POWER_HELP_MODE
# Switch to energy-efficient assistance when battery is low

def glyph_636(battery_level, threshold=20):
    return 'low_power_assist' if battery_level < threshold else 'normal'
