# glyph_739 – AUTO_DOC_SYNTH
# Synthesize markdown docs from function signatures and docstrings.

import inspect

def glyph_739(module_obj):
    """
    Returns markdown string documenting callables in a module-like object.
    """
    lines = ["# API Documentation", ""]
    for name, obj in inspect.getmembers(module_obj, inspect.isfunction):
        sig = str(inspect.signature(obj))
        doc = (inspect.getdoc(obj) or "").strip()
        lines.append(f"## {name}{sig}\n\n{doc}\n")
    return "\n".join(lines)
