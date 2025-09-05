# glyph_597 – SECURE_AUTH_CHAIN
# Build a chain of authentication steps

def glyph_597(user, steps):
    results = []
    for step in steps:
        if not step(user):
            results.append(False)
            break
        results.append(True)
    return all(results)
