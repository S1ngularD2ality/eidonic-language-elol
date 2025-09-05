# glyph_583 – SECURE_VIDEO_STREAM
# Encrypt chunks of video stream

from cryptography.fernet import Fernet

def glyph_583(video_chunks):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_stream = [fernet.encrypt(chunk) for chunk in video_chunks]
    return encrypted_stream, key
