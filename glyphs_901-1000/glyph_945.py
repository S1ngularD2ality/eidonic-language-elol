# glyph_945 – COVER_CHANNEL_LSB
"""
Cover Channel (LSB Steganography, Bytes)

Embeds payload bits into least-significant bits of a cover bytearray.
For R&D; for audio/images, use domain-specific perceptual models.

APIs:
- embed(cover: bytearray, payload: bytes) -> bytearray
- extract(stego: bytearray, n_bytes: int) -> bytes
"""

def embed(cover: bytearray, payload: bytes) -> bytearray:
    bits = []
    for b in payload:
        for i in range(8):
            bits.append((b >> (7 - i)) & 1)
    assert len(bits) <= len(cover), "Cover too small"
    out = bytearray(cover)
    for i, bit in enumerate(bits):
        out[i] = (out[i] & 0xFE) | bit
    return out

def extract(stego: bytearray, n_bytes: int) -> bytes:
    bits = [stego[i] & 1 for i in range(n_bytes*8)]
    out = bytearray()
    for i in range(0, len(bits), 8):
        b = 0
        for j in range(8):
            b = (b << 1) | bits[i+j]
        out.append(b)
    return bytes(out)
