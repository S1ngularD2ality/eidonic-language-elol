# glyph_940 – TIMELINE_NOTARY
"""
Timeline Notary (append-only, time-bound attestations)

Each notarization binds (timestamp || payload_hash) into a running Merkle chain.
Outputs a receipt containing (leaf, proof, root). Verifiers check consistency.

APIs:
- class TimelineNotary: add(payload) -> receipt, root
- verify(payload, receipt, root) -> bool
"""

import time, hashlib
from typing import List, Tuple

def _H(x: bytes) -> bytes:
    return hashlib.blake2b(x, digest_size=32).digest()

class TimelineNotary:
    def __init__(self):
        self.leaves: List[bytes] = []

    def add(self, payload: bytes) -> Tuple[dict, bytes]:
        ts = int(time.time_ns()).to_bytes(8, "big")
        leaf = _H(ts + _H(payload))
        self.leaves.append(leaf)
        root, nodes = self._build()
        proof = self._prove(len(self.leaves)-1, nodes)
        receipt = {"ts": int.from_bytes(ts, "big"), "leaf": leaf.hex(), "proof": [(s.hex(), r) for s, r in proof]}
        return receipt, root

    def _build(self) -> Tuple[bytes, List[List[bytes]]]:
        level = self.leaves[:]
        if not level: return b"\x00"*32, [level]
        nodes = [level]
        while len(level) > 1:
            nxt=[]
            for i in range(0, len(level), 2):
                a = level[i]
                b = level[i+1] if i+1 < len(level) else a
                nxt.append(_H(a+b))
            level = nxt
            nodes.append(level)
        return level[0], nodes

    def _prove(self, index: int, nodes: List[List[bytes]]) -> List[Tuple[bytes,bool]]:
        proof=[]
        idx = index
        for lvl in nodes[:-1]:
            sib = idx ^ 1
            if sib >= len(lvl): sib = idx
            proof.append((lvl[sib], sib > idx))
            idx //= 2
        return proof

def verify(payload: bytes, receipt: dict, root: bytes) -> bool:
    ts = int(receipt["ts"]).to_bytes(8, "big")
    leaf = bytes.fromhex(receipt["leaf"])
    if leaf != _H(ts + _H(payload)): return False
    h = leaf
    for s_hex, right in receipt["proof"]:
        s = bytes.fromhex(s_hex)
        h = _H(h+s) if right else _H(s+h)
    return h == root
