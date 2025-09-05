# glyph_562 – SIGN_MESSAGE
# Create a digital signature for a message

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def glyph_562(private_key, message):
    return private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
