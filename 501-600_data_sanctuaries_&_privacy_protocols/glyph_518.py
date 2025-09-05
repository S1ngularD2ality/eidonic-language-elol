# glyph_518 – DATA_WIPE
# Overwrite data with random bytes before deletion

import os

def glyph_518(file_path):
    size = os.path.getsize(file_path)
    with open(file_path, 'wb') as f:
        f.write(os.urandom(size))
    os.remove(file_path)
