# glyph_753 – INTEGRITY_VERIFIER
# Verify checksum of data blocks.

import hashlib

def glyph_753(data_blocks):
    """
    data_blocks: list of (data, expected_checksum)
    Returns: list of bool results
    """
    results = []
    for data, expected in data_blocks:
        actual = hashlib.sha256(data).hexdigest()
        results.append(actual == expected)
    return results
