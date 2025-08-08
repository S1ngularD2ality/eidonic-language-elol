# glyph_671 – NON_INTRUSIVE_MONITOR
# Monitor without recording personal data

def glyph_671(sensor_data):
    return {k: v for k, v in sensor_data.items() if k not in ['faces', 'voices']}
