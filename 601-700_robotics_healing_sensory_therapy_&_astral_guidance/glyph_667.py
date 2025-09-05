# glyph_667 – MEDICAL_SCAN_MODE
# Switch sensors to detect health vitals

def glyph_667(is_scan_active):
    return 'medical_scan' if is_scan_active else 'normal'
