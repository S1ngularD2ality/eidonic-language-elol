# glyph_657 – BOT_HEALTH_MONITOR
# Monitor internal system health for preventive maintenance

def glyph_657(status_report):
    return {k: v for k, v in status_report.items() if v != 'OK'}
