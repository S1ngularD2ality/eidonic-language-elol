# glyph_396 – ACTUATOR_DIAG
# Diagnose actuator/motor health and recommend maintenance

def glyph_396(actuator_data):
    """
    actuator_data: dict with 'temp', 'vibration', 'load'
    Returns: 'healthy', 'warn', or 'fail'
    """
    if actuator_data['temp'] > 90 or actuator_data['vibration'] > 0.5:
        return "fail"
    if actuator_data['load'] > 0.8:
        return "warn"
    return "healthy"
