# glyph_426 – SIGNAL_GUARD
# Secure, encrypt, and authenticate all signals in an agent collective

def glyph_426(signal, key="s3cr3t"):
    """
    signal: string
    key: encryption key
    Returns: encrypted signal (simulated)
    """
    import hashlib
    return hashlib.sha256((signal + key).encode()).hexdigest()
