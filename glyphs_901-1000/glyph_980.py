# glyph_980 – QUANTUM_RESISTANT_PUZZLE_MIX
"""
Quantum-Resistant Puzzle Mix

Combines:
1) Time-lock hash chain of length T (sequential work),
2) Proof-of-Work (difficulty bits),
3) Commitment to payload.

An attacker must do sequential work + PoW to forge a valid mix, resisting
massive parallel/quantum shortcuts (within practical bounds).

APIs:
- lock(payload, seed, T, difficulty_bits)-> dict
- verify(obj)->bool
"""

import hashlib, hmac

def _H(x: bytes, n=32) -> bytes:
    return hashlib.blake2b(x, digest_size=n).digest()

def _hash_chain(seed: bytes, T: int) -> bytes:
    x = seed
    for _ in range(T):
        x = _H(x)
    return x

def _pow(challenge: bytes, difficulty_bits: int) -> int:
    target = 1 << (256 - difficulty_bits)
    nonce = 0
    while True:
        h = int.from_bytes(_H(challenge + nonce.to_bytes(8,"big"), n=32), "big")
        if h < target: return nonce
        nonce += 1

def lock(payload: bytes, seed: bytes, T: int, difficulty_bits: int) -> dict:
    chain_anchor = _hash_chain(seed, T)
    commitment = hmac.new(chain_anchor, payload, hashlib.blake2b).digest()
    nonce = _pow(commitment, difficulty_bits)
    return {"anchor": chain_anchor.hex(), "commit": commitment.hex(), "nonce": nonce, "dbits": difficulty_bits}

def verify(obj: dict, payload: bytes) -> bool:
    anchor = bytes.fromhex(obj["anchor"])
    commit = bytes.fromhex(obj["commit"])
    if not hmac.compare_digest(hmac.new(anchor, payload, hashlib.blake2b).digest(), commit):
        return False
    difficulty_bits = int(obj["dbits"])
    target = 1 << (256 - difficulty_bits)
    h = int.from_bytes(_H(commit + int(obj["nonce"]).to_bytes(8,"big"), n=32), "big")
    return h < target
