# glyph_432 – FEEDBACK_LOOP
# Create continuous feedback cycles for rapid improvement or error correction

def glyph_432(process, initial_input, rounds=3):
    """
    process: callable
    initial_input: any
    rounds: int
    Returns: final output
    """
    result = initial_input
    for _ in range(rounds):
        result = process(result)
    return result
