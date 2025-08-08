# glyph_527 – TWO_FACTOR_VERIFY
# Verify a two-factor code within a time window

import time

class glyph_527:
    def __init__(self):
        self.codes = {}

    def generate(self, user):
        code = str(time.time())[-6:]
        self.codes[user] = (code, time.time())
        return code

    def verify(self, user, code, window=30):
        if user in self.codes:
            stored_code, timestamp = self.codes[user]
            if stored_code == code and (time.time() - timestamp) <= window:
                return True
        return False
