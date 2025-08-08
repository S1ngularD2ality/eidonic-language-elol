# glyph_537 – SECURE_TOKEN_ROTATE
# Rotate API tokens for security

import secrets

def glyph_537(token_store, user):
    new_token = secrets.token_urlsafe(32)
    token_store[user] = new_token
    return token_store
