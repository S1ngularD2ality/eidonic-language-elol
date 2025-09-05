# glyph_529 – MASK_EMAIL
# Mask an email address to hide identity

def glyph_529(email):
    name, domain = email.split("@")
    return f"{name[0]}***@{domain}"
