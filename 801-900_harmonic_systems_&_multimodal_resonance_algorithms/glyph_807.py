# glyph_807 – FLOWER_OF_LIFE_COMPRESSION
# Lossless compression/decompression using zlib.

import zlib

def glyph_807_compress(data: bytes) -> bytes:
    return zlib.compress(data)

def glyph_807_decompress(blob: bytes) -> bytes:
    return zlib.decompress(blob)
