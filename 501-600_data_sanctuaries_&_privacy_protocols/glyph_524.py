# glyph_524 – SECURE_WIPE_DIR
# Securely wipe all files in a directory

import os

def glyph_524(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            with open(filepath, 'wb') as f:
                f.write(os.urandom(size))
            os.remove(filepath)
