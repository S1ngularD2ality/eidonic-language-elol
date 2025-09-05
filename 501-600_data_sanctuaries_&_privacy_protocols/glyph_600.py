# glyph_600 – ZERO_TRUST_VALIDATE
# Validate access with zero trust principle

def glyph_600(user, resource, policies):
    for policy in policies:
        if not policy(user, resource):
            return False
    return True
