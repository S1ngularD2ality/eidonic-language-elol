# glyph_350 – ANOMALY_ALERT
# Detect anomalies or unexpected patterns in any sensory stream

def glyph_350(data_stream):
    """
    data_stream: list of numeric values
    Returns: True if anomaly detected
    """
    import numpy as np
    mean = np.mean(data_stream)
    std = np.std(data_stream)
    for value in data_stream:
        if abs(value - mean) > 3 * std:
            return True
    return False
