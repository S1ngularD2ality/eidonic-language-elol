# glyph_506 – SIG_VERIFY
# Verify a digital signature using RSA public key

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def glyph_506(public_key, message, signature):
    public_key.verify(
        signature,
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return True
