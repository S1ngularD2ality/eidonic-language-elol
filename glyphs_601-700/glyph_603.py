# glyph_603 – HUMAN_PRESENCE_DETECT
# Detect human presence from sensor data

def glyph_603(sensor_data, threshold=0.8):
    return any(val > threshold for val in sensor_data.values())
