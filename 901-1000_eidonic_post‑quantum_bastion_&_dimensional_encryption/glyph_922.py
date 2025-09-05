# glyph_922 – MERKLE_TREE_AND_PROOF
"""
Merkle Tree (BLAKE2b) with proof generation/verification.

APIs:
- build(leaves: List[bytes]) -> (root: bytes, nodes: List[List[bytes]])
- prove(leaves, index) -> List[(sibling: bytes, is_right: bool)]
- verify(leaf: bytes, index: int, proof, root: bytes) -> bool
"""

import hashlib
from typing import List, Tuple

def _h(x: bytes) -> bytes:
    return hashlib.blake2b(x, digest_size=32).digest()

def build(leaves: List[bytes]) -> Tuple[bytes, List[List[bytes]]]:
    assert leaves
    level = [_h(b"\x00"+l) for l in leaves]
    nodes = [level]
    while len(level) > 1:
        nxt = []
        for i in range(0, len(level), 2):
            a = level[i]
            b = level[i+1] if i+1 < len(level) else a
            nxt.append(_h(b"\x01"+a+b))
        level = nxt
        nodes.append(level)
    return level[0], nodes

def prove(leaves: List[bytes], index: int) -> List[Tuple[bytes, bool]]:
    root, nodes = build(leaves)
    proof = []
    idx = index
    for lvl in nodes[:-1]:
        sib = idx ^ 1
        if sib >= len(lvl): sib = idx
        proof.append((lvl[sib], sib > idx))
        idx //= 2
    return proof

def verify(leaf: bytes, index: int, proof: List[Tuple[bytes, bool]], root: bytes) -> bool:
    h = _h(b"\x00"+leaf)
    idx = index
    for sib, is_right in proof:
        if is_right:
            h = _h(b"\x01"+h+sib)
        else:
            h = _h(b"\x01"+sib+h)
        idx //= 2
    return h == root
