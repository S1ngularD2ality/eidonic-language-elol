# glyph_322 – HEAT_SHADOW
# Perceive and track temperature gradients in space for safe movement or object finding

def glyph_322(thermal_data):
    """
    thermal_data: dict of (x,y):temp_value
    Returns: zones of heat, cold, and anomalies
    """
    hot_spots = [k for k, v in thermal_data.items() if v > 30]
    cold_spots = [k for k, v in thermal_data.items() if v < 5]
    return {'hot': hot_spots, 'cold': cold_spots}
