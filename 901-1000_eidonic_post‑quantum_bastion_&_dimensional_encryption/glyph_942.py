# glyph_942 – ORAM_PATH_MINI
"""
Path-ORAM (Mini, Educational Sketch)

Maintains an encrypted array abstraction where access patterns are
obfuscated by reading/writing along random root-to-leaf paths (buckets).
This is a *very* simplified model for R&D; production ORAM requires
careful eviction and stash management.

APIs:
- class MiniPathORAM: get(idx)->bytes, put(idx, val)->None
"""

import os, random

class MiniPathORAM:
    def __init__(self, n_blocks: int, block_size: int = 64, buckets_per_path: int = 4):
        self.n = n_blocks
        self.bs = block_size
        self.h = buckets_per_path
        self.pos = {i: random.randrange(2**(self.h-1)) for i in range(n_blocks)}
        self.tree = [[os.urandom(block_size) for _ in range(2)] for _ in range(self.h)]
        self.store = {i: os.urandom(block_size) for i in range(n_blocks)}  # encrypted blocks

    def _path_nodes(self, leaf):
        # Return indices along a fake path; toy: two nodes per level
        return [(lvl, leaf % 2) for lvl in range(self.h)]

    def get(self, idx: int) -> bytes:
        leaf = self.pos[idx]
        path = self._path_nodes(leaf)
        _ = [self.tree[l][b] for (l, b) in path]  # read path (noise)
        # Move position
        self.pos[idx] = random.randrange(2**(self.h-1))
        return self.store[idx]

    def put(self, idx: int, val: bytes):
        assert len(val) == self.bs
        leaf = self.pos[idx]
        path = self._path_nodes(leaf)
        _ = [self.tree[l][b] for (l, b) in path]  # read path (noise)
        self.pos[idx] = random.randrange(2**(self.h-1))
        self.store[idx] = val
