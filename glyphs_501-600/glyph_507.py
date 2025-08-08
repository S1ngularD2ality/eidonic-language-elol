# glyph_507 – INTRUSION_ALERT
# Trigger alert if data access is from unknown source

def glyph_507(access_logs, trusted_sources):
    return [log for log in access_logs if log['source'] not in trusted_sources]
