def context_oracle(image_data):
    """
    Returns environment label: 'kitchen', 'factory', etc.
    """
    import random
    labels = ['kitchen', 'factory', 'hospital', 'outdoor', 'lab']
    return random.choice(labels)  # Replace with ML classifier for real use
