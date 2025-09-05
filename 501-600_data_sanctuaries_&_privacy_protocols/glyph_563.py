# glyph_563 – VERIFY_SIGNATURE
# Verify a digital signature for a message

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def glyph_563(public_key, message, signature):
    public_key.verify(
        signature,
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return True
