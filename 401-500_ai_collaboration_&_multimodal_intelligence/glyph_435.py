# glyph_435 – MULTIMODAL_ALERT
# Trigger urgent alerts using all available modalities (sound, text, light, haptic)

def glyph_435(modalities, alert_msg):
    """
    modalities: list of strings
    alert_msg: string
    Returns: dict of modality:alert
    """
    return {m: alert_msg for m in modalities}
