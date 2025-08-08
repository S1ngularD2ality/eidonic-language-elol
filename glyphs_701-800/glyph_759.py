# glyph_759 – SYSTEM_DEPENDENCY_CHECKER
# Verify all required dependencies are installed.

import importlib

def glyph_759(required_modules):
    """
    Returns: dict module->bool
    """
    status = {}
    for m in required_modules:
        try:
            importlib.import_module(m)
            status[m] = True
        except ImportError:
            status[m] = False
    return status
