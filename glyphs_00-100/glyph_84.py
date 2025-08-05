import random

def mirror_cast(n):
    """
    Randomly selects mirror outcomes.

    Parameters:
        n (int)

    Returns:
        List[str]
    """
    return [random.choice(['🪞', '🔥', '💧']) for _ in range(n)]
