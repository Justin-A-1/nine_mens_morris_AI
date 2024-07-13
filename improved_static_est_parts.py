from building_blocks import *
#from collections import Counter

def countPotentialMills(board: str, piece: str) -> int:
    """
    Count the number of potential mills that can be formed by adding one more piece.

    Args:
        board (str): The current board position as a string.
        piece (str): The piece type to count potential mills for ('B' or 'W').

    Returns:
        int: The number of potential mills.
    """
    potential_mills = 0

    for mill in closeMillCoords:
        pieces_in_mill = [board[coordToIndexDict[coord]] for coord in mill]
        if pieces_in_mill.count(piece) == 2 and pieces_in_mill.count('x') == 1:
            potential_mills += 1

    return potential_mills

def countBlockedPieces(board: str, piece: str) -> int:
    """
    Count the number of blocked pieces for a given piece type.

    Args:
        board (str): The current board position as a string.
        piece (str): The piece type to count blocked pieces for ('B' or 'W').

    Returns:
        int: The number of blocked pieces.
    """
    blocked_pieces = 0

    for i, spot in enumerate(board):
        if spot == piece:
            neighbors = neighborsDict[indexToCoordDict[i]]
            if all(board[coordToIndexDict[neighbor]] != 'x' for neighbor in neighbors):
                blocked_pieces += 1

    return blocked_pieces

# Count frequency of positions in mills
#position_frequency_in_mills = Counter()
#for mill in closeMillCoords:
#    position_frequency_in_mills.update(mill)

# Print the number of mills each coordinate appears in
#print("Number of mills each coordinate appears in:")
#for coord, count in position_frequency_in_mills.items():
#    print(f"{coord}: {count}")

positions_three_mills = {'e4', 'f5', 'g6'}
positions_one_mill = {'a0', 'b1', 'c2'}
positions_two_mills = set(coordToIndexDict.keys()) - positions_three_mills - positions_one_mill
positions_four_neighbors = {'b1', 'f1', 'f3', 'b5', 'd5', 'f5'}

def countThreeMillPositions(board: str, piece: str) -> int:
    return sum(1 for pos in positions_three_mills if board[coordToIndexDict[pos]] == piece)

def countOneMillPositions(board: str, piece: str) -> int:
    return sum(1 for pos in positions_one_mill if board[coordToIndexDict[pos]] == piece)

def countFourNeighborPositions(board: str, piece: str) -> int:
    return sum(1 for pos in positions_four_neighbors if board[coordToIndexDict[pos]] == piece)

def isPartOfMill(position: str, board: str, piece: str) -> bool:
    """
    Check if a given position is part of a mill for a specific piece type.

    Args:
        position (str): The coordinate to check.
        board (str): The current board position as a string.
        piece (str): The piece type to check for ('B' or 'W').

    Returns:
        bool: True if the position is part of a mill, False otherwise.
    """
    for mill in closeMillCoords:
        if position in mill:
            if all(board[coordToIndexDict[coord]] == piece for coord in mill):
                return True
    return False

def countUnsafePieces(board: str, piece: str) -> int:
    """
    Count the number of pieces of the given type that are not safely in a mill.

    Args:
        board (str): The current board position as a string.
        piece (str): The piece type to count unsafe pieces for ('B' or 'W').

    Returns:
        int: The number of unsafe pieces.
    """
    unsafe_pieces = 0

    for i, spot in enumerate(board):
        if spot == piece:
            coord = indexToCoordDict[i]
            if not isPartOfMill(coord, board, piece):
                unsafe_pieces += 1

    return unsafe_pieces