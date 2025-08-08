# glyph_523 – SAFE_CHANNEL
# Create encrypted communication pipeline

from cryptography.fernet import Fernet

class glyph_523:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def send(self, message):
        return self.fernet.encrypt(message.encode())

    def receive(self, token):
        return self.fernet.decrypt(token).decode()
