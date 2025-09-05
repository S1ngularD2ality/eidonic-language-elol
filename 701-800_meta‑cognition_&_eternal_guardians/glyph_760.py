# glyph_760 – AI_SELF_PRESERVATION_PROTOCOL
# Protect critical data and processes from loss.

import shutil
import os

class glyph_760:
    def __init__(self, backup_dir):
        self.backup_dir = backup_dir
        os.makedirs(backup_dir, exist_ok=True)

    def backup_file(self, path):
        if os.path.isfile(path):
            shutil.copy(path, self.backup_dir)

    def restore_file(self, filename, target_dir):
        src = os.path.join(self.backup_dir, filename)
        if os.path.isfile(src):
            shutil.copy(src, target_dir)
