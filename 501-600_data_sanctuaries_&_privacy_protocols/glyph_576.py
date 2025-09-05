# glyph_576 – DECRYPT_LOG_STREAM
# Decrypt logs encrypted by glyph_575

class glyph_576:
    def __init__(self, key, logs):
        from cryptography.fernet import Fernet
        self.fernet = Fernet(key)
        self.logs = logs

    def read_logs(self):
        return [self.fernet.decrypt(log).decode() for log in self.logs]
