# glyph_719 – DEEP_SELF_DIAGNOSTIC
# Full-stack self-check across modules with structured results.

def glyph_719(checks):
    """
    checks: dict name->callable() returning True/False or raising
    Returns: {'passed':[names], 'failed':[names], 'errors':{name:str}}
    """
    passed, failed, errors = [], [], {}
    for name, fn in checks.items():
        try:
            ok = bool(fn())
            (passed if ok else failed).append(name)
        except Exception as e:
            errors[name] = str(e)
    return {"passed": passed, "failed": failed, "errors": errors}
