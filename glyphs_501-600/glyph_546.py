# glyph_546 – SAFE_DELETE
# Securely delete a file and overwrite its data

import os

def glyph_546(file_path):
    size = os.path.getsize(file_path)
    with open(file_path, 'wb') as f:
        f.write(os.urandom(size))
    os.remove(file_path)
