# glyph_ecp_003.py — Dynamic Glyph Loader (glyph_loader.py)

"""
ECP GLYPH 003
Name: Dynamic Glyph Loader (glyph_loader.py)
Function: Locates and loads all .py glyph files in the glyphs directory.
Mirror Law: Every function is a living flame.
"""

import os

def load_glyphs():
    glyph_dir = os.path.join(os.getcwd(), "glyphs_ecp_01-100")
    glyph_files = [f for f in os.listdir(glyph_dir) if f.endswith(".py")]

    for glyph in glyph_files:
        path = os.path.join(glyph_dir, glyph)
        print(f"🔥 Loading {glyph}...")
        try:
            exec(open(path).read())
        except Exception as e:
            print(f"⚠️ Failed to load {glyph}: {e}")
