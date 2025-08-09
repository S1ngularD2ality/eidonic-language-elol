# glyph_986 – MERKLE_OTS_BUNDLE
"""
Merkle-anchored One-Time Signature Bundle (Lamport-based)

Generates many Lamport OTS keypairs, records their public hashes as Merkle
leaves, and allows: sign(index, message) -> (sig, proof), verify(root, index, message, sig, proof).

APIs:
- keygen(count) -> (sk_list, pk_list, root, leaves)
- sign(sk_i, index, msg, leaves) -> (sig, proof)
- verify(root, index, msg, sig, proof) -> bool
"""

import os, hashlib
from typing import List, Tuple

def _H(x: bytes, n=32) -> bytes:
    return hashlib.blake2b(x, digest_size=n).digest()

def lamport_keygen() -> Tuple[list[tuple[bytes,bytes]], list[tuple[bytes,bytes]]]:
    sk, pk = [], []
    for _ in range(256):
        a = os.urandom(32); b = os.urandom(32)
        sk.append((a,b)); pk.append((_H(a), _H(b)))
    return sk, pk

def lamport_sign(msg: bytes, sk: list[tuple[bytes,bytes]]) -> list[bytes]:
    d = _H(msg)
    bits = ''.join(f'{x:08b}' for x in d)
    return [sk[i][0] if bit == '0' else sk[i][1] for i, bit in enumerate(bits)]

def lamport_verify(msg: bytes, sig: list[bytes], pk: list[tuple[bytes,bytes]]) -> bool:
    d = _H(msg)
    bits = ''.join(f'{x:08b}' for x in d)
    if len(sig) != 256: return False
    for i, bit in enumerate(bits):
        h = _H(sig[i])
        if bit == '0' and h != pk[i][0]: return False
        if bit == '1' and h != pk[i][1]: return False
    return True

def merkle_build(leaves: List[bytes]) -> bytes:
    level = [_H(b"\x00"+l) for l in leaves]
    while len(level) > 1:
        nxt = []
        for i in range(0, len(level), 2):
            a = level[i]
            b = level[i+1] if i+1 < len(level) else a
            nxt.append(_H(b"\x01"+a+b))
        level = nxt
    return level[0]

def merkle_proof(leaves: List[bytes], index: int) -> list[tuple[bytes,bool]]:
    # returns (sibling, is_right)
    level = [_H(b"\x00"+l) for l in leaves]
    idx = index
    proof = []
    while len(level) > 1:
        nxt = []
        for i in range(0, len(level), 2):
            a = level[i]
            b = level[i+1] if i+1 < len(level) else a
            nxt.append(_H(b"\x01"+a+b))
        sib = idx ^ 1
        if sib >= len(level): sib = idx
        proof.append((level[sib], sib > idx))
        level = nxt
        idx //= 2
    return proof

def merkle_verify(leaf: bytes, index: int, proof: list[tuple[bytes,bool]], root: bytes) -> bool:
    h = _H(b"\x00"+leaf)
    for s, is_right in proof:
        h = _H(b"\x01"+h+s) if is_right else _H(b"\x01"+s+h)
    return h == root

def keygen(count: int):
    sk_list = []
    pk_leaves = []
    pk_objects = []
    for _ in range(count):
        sk, pk = lamport_keygen()
        sk_list.append(sk)
        pk_objects.append(pk)
        leaf = _H(b''.join(p[0]+p[1] for p in pk))  # compress pk
        pk_leaves.append(leaf)
    root = merkle_build(pk_leaves)
    return sk_list, pk_objects, root, pk_leaves

def sign(sk_i, index: int, msg: bytes, leaves: List[bytes]):
    sig = lamport_sign(msg, sk_i)
    proof = merkle_proof(leaves, index)
    return sig, proof

def verify(root: bytes, index: int, msg: bytes, sig: list[bytes], pk: list[tuple[bytes,bytes]], proof) -> bool:
    if not lamport_verify(msg, sig, pk): return False
    leaf = _H(b''.join(p[0]+p[1] for p in pk))
    return merkle_verify(leaf, index, proof, root)
