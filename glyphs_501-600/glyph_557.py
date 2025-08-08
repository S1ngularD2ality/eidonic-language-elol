# glyph_557 – SECURE_BROADCAST
# Broadcast encrypted message to multiple recipients

from cryptography.fernet import Fernet

def glyph_557(message, recipients):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return {recipient: encrypted_message for recipient in recipients}, key
