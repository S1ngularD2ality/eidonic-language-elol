# glyph_517 – IP_BLOCK
# Block access from a specific IP address

def glyph_517(ip, blocklist):
    blocklist.add(ip)
    return blocklist
