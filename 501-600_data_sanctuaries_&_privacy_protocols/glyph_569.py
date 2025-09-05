# glyph_569 – SECURE_RANDOM_STRING
# Generate secure random string of given length

import secrets
import string

def glyph_569(length=16):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))
