# glyph_551 – SANDBOX_EXEC
# Execute code in a restricted sandbox environment

def glyph_551(code):
    allowed_builtins = {'print': print, 'len': len}
    exec(code, {"__builtins__": allowed_builtins})
