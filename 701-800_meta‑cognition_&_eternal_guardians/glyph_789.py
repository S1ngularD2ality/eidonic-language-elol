# glyph_789 – MULTI_LAYER_AUTH
# Requires multiple independent authentications.

def glyph_789(auth_methods):
    return all(method() for method in auth_methods)
