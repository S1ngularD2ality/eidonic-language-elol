# glyph_522 – DEEP_LOG_SCAN
# Scan logs for security anomalies

def glyph_522(logs, anomaly_keywords):
    return [entry for entry in logs if any(k in entry for k in anomaly_keywords)]
