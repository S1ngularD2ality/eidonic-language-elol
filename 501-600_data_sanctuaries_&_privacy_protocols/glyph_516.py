# glyph_516 – LOG_PURGE
# Securely erase log files to prevent recovery

import os

def glyph_516(file_path):
    with open(file_path, 'ba+', buffering=0) as f:
        length = f.tell()
    with open(file_path, 'br+') as f:
        f.write(os.urandom(length))
    os.remove(file_path)
