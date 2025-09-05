# glyph_941 – OBLIVIOUS_PIR_XOR
"""
Oblivious PIR (XOR-Style, Toy Demonstrator)

Goal: Client retrieves record i from a server-stored database without revealing i.
This toy scheme assumes: database is a list of equal-length byte-rows and
the server supports masked XOR retrieval (no index leakage beyond mask length).

Mechanics (toy):
- Client builds a binary mask vector m of len=N with ~k ones (k>1) s.t. i is among them.
- Server XORs all rows where m[j]==1 and returns the XOR. Client pre-holds XOR of all
  masked rows *except* i (from cached snapshots or second server), then XORs again to recover row i.
- In practice, use multi-server or computational PIR; this is a structural sketch for integration.

APIs:
- server_xor_mask(db: List[bytes], mask: List[int]) -> bytes
"""

from typing import List

def server_xor_mask(db: List[bytes], mask: List[int]) -> bytes:
    assert len(db) == len(mask) and len(db) > 0
    L = len(db[0])
    acc = bytearray([0]*L)
    for row, bit in zip(db, mask):
        assert len(row) == L
        if bit:
            acc = bytearray(a ^ b for a, b in zip(acc, row))
    return bytes(acc)
