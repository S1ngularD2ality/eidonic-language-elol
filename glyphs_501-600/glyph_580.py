# glyph_580 – SECURE_KEY_SHARE
# Securely share an encryption key using public key cryptography

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def glyph_580(public_key_pem, key_to_share):
    public_key = serialization.load_pem_public_key(public_key_pem)
    encrypted_key = public_key.encrypt(
        key_to_share,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return encrypted_key
