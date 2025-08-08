# glyph_508 – SECURE_CHANNEL
# Establish a secure HTTPS connection

import requests

def glyph_508(url):
    response = requests.get(url, verify=True)
    return response.status_code, response.text
