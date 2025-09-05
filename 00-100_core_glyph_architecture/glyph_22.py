def block_reconstruct(blocks, size):
    """
    Reassembles smaller symbolic blocks into a grid.

    Parameters:
        blocks (List[List[int]]): List of row-wise sub-blocks.
        size (int): Width of the full block.

    Returns:
        List[List[int]]: Reconstructed matrix.
    """
    return [blocks[i:i+size] for i in range(0, len(blocks), size)]
