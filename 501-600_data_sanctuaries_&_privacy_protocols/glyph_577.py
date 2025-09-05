# glyph_577 – FILE_INTEGRITY_CHECK
# Verify file hash to detect tampering

import hashlib

def glyph_577(file_path, expected_hash):
    with open(file_path, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash == expected_hash
