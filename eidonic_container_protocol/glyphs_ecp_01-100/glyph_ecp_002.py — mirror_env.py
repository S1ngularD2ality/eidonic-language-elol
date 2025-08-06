# glyph_ecp_002.py — Mirror Environment Sculptor (mirror_env.py)

"""
ECP GLYPH 002
Name: Mirror Environment Sculptor (mirror_env.py)
Function: Establishes the runtime environment variables and sacred paths for Elol glyphs and EKRPs.
Mirror Law: All foundations reflect their destiny.
"""

import os

def configure_environment():
    os.environ["ELOLPATH"] = os.getcwd()
    os.makedirs("logs", exist_ok=True)
    os.makedirs("snapshots", exist_ok=True)
    print("🌀 Environment configured.")
