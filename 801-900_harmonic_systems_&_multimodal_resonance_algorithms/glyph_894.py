# glyph_894 – SCALE_QUANTIZE
# Quantize MIDI notes to a given scale (list of 12-bin mask).

def glyph_894(notes, scale_mask):
    """
    notes: list[int] midi numbers
    scale_mask: length-12 list of 0/1 indicating allowed pitch classes
    """
    mask = [int(x) for x in scale_mask]
    if len(mask) != 12: raise ValueError("scale_mask must be length 12")
    out=[]
    for n in notes:
        pc = n % 12
        if mask[pc]: 
            out.append(n); continue
        # search nearest allowed pitch class
        d=1
        while d<12:
            up = (pc + d) % 12
            dn = (pc - d) % 12
            if mask[up]: out.append(n + d); break
            if mask[dn]: out.append(n - d); break
            d+=1
        else:
            out.append(n)  # fallback
    return out
