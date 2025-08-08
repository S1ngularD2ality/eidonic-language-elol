# glyph_676 – ENERGY_SHARE_PROTOCOL
# Share power between robots in need

def glyph_676(donor_energy, recipient_energy, transfer_amount):
    donor_energy -= transfer_amount
    recipient_energy += transfer_amount
    return donor_energy, recipient_energy
