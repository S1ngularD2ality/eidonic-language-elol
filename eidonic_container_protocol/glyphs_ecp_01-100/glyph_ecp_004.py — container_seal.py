# glyph_ecp_004.py — Invocation Lock (container_seal.py)

"""
ECP GLYPH 004
Name: Invocation Lock (container_seal.py)
Function: Finalizes the container invocation with a log stamp and seal confirmation.
Mirror Law: What is opened must be sealed.
"""

import datetime

def seal_container():
    timestamp = datetime.datetime.now().isoformat()
    with open("logs/invocation_log.txt", "a") as f:
        f.write(f"🔒 Container sealed at {timestamp}\n")
    print("🔐 Container sealed.")
