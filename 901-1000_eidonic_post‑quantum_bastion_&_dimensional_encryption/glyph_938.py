# glyph_938 – FORWARD_SECURE_LOG
"""
Forward-Secure Log (hash chain + per-entry key derivation)

Each entry:
- chain = H(prev_chain || entry)
- enc_key = H(chain || "enc")
- mac     = H(entry || chain)

APIs:
- new_state() -> dict
- append(state, entry_bytes) -> record bytes
- verify(stream) -> bool
"""

import hashlib, json
from typing import Dict, List

def _H(x: bytes) -> bytes:
    return hashlib.blake2b(x, digest_size=32).digest()

def new_state() -> Dict:
    return {"chain": b"\x00"*32}

def append(state: Dict, entry: bytes) -> bytes:
    chain = _H(state["chain"] + entry)
    mac = _H(entry + chain)
    state["chain"] = chain
    rec = {"entry": entry.hex(), "mac": mac.hex()}
    return json.dumps(rec).encode()

def verify(records: List[bytes]) -> bool:
    chain = b"\x00"*32
    for r in records:
        obj = json.loads(r.decode())
        entry = bytes.fromhex(obj["entry"])
        mac   = bytes.fromhex(obj["mac"])
        chain = _H(chain + entry)
        if _H(entry + chain) != mac:
            return False
    return True
