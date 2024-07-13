# includes closeMill, generateRemove, GenerateAdd, GenerateMovesOpening, GenerateHopping
# includes neighbors, GenerateMove, GenerateMovesMidgameEndgame

indexToCoordDict = {
    0: 'a0',
    1: 'g0',        
    2: 'b1',        
    3: 'f1',        
    4: 'c2',
    5: 'e2',
    6: 'e3',
    7: 'f3',
    8: 'g3',
    9: 'c4',
    10: 'd4',
    11: 'e4',
    12: 'b5',
    13: 'd5',
    14: 'f5',
    15: 'a6',
    16: 'd6',
    17: 'g6'
}

coordToIndexDict = {
    'a0': 0,
    'g0': 1,        
    'b1': 2,        
    'f1': 3,        
    'c2': 4,
    'e2': 5,
    'e3': 6,
    'f3': 7,
    'g3': 8,
    'c4': 9,
    'd4': 10,
    'e4': 11,
    'b5': 12,
    'd5': 13,
    'f5': 14,
    'a6': 15,
    'd6': 16,
    'g6': 17
}

closeMillCoords = [
    ['a0', 'b1', 'c2'],
    ['e2', 'f1', 'g0'],
    ['e3', 'f3', 'g3'],
    ['e4', 'f5', 'g6'],
    ['d4', 'd5', 'd6'],
    ['a6', 'b5', 'c4'],

    ['a6', 'd6', 'g6'],
    ['b5', 'd5', 'f5'],
    ['c4', 'd4', 'e4'],
    ['e4', 'e3', 'e2'],
    ['f5', 'f3', 'f1'],
    ['g6', 'g3', 'g0']
]

neighborsDict = {
    'a0': ['g0','b1','a6'],
    'g0': ['a0','f1','g3'],        
    'b1': ['a0','f1','c2','b5'],        
    'f1': ['g0','b1','e2','f3'],        
    'c2': ['b1','e2','c4'],
    'e2': ['f1','c2','e3'],
    'e3': ['e2','f3','e4'],
    'f3': ['f1','e3','g3','f5'],
    'g3': ['g0','f3','g6'],
    'c4': ['c2','d4','b5'],
    'd4': ['c4','e4','d5'],
    'e4': ['e3','d4','f5'],
    'b5': ['b1','c4','d5','a6'],
    'd5': ['d4','b5','f5','d6'],
    'f5': ['f3','e4','d5','g6'],
    'a6': ['a0','b5','d6'],
    'd6': ['d5','a6','g6'],
    'g6': ['g3','f5','d6']
}

def closeMill(j: int, b: str) -> bool:
    """
    Checks if the given position on the board closes a mill.

    Args:
        j (int): The index of the position to check.
        b (str): The current board state represented as a string.

    Returns:
        bool: True if the position closes a mill, False otherwise.
    """
    if b[j] not in ['W', 'B']:
        return False
    coord_j = indexToCoordDict[j]
    for mill in closeMillCoords:
        if coord_j in mill:
            other_coords = [c for c in mill if c != coord_j]
            m = coordToIndexDict[other_coords[0]]
            n = coordToIndexDict[other_coords[1]]

            if b[m] == b[j] and b[n] == b[j]:
                return True
    return False    

def GenerateRemove(board: str, L: list) -> None:
    """
    Generate new board positions by removing black pieces and add them to L.

    Args:
        board (str): The current board position as a string.
        L (list): The list to add new board positions to.
    """
    positions_added = False

    for location in range(len(board)):
        if board[location] == 'B':
            if not closeMill(location, board):
                b = board[:location] + 'x' + board[location + 1:]  # Create a new board string with the black piece removed
                L.append(b)  # Add the new board position to L
                positions_added = True


    if not positions_added:
        L.append(board)  # Add the input board position if no positions were added

def GenerateAdd(board: str) -> list:
    """
    Generate new board positions by adding a white piece and return the list of positions.

    Args:
        board (str): The current board position as a string.

    Returns:
        list: A list of new board positions.
    """
    L = []

    for location in range(len(board)):
        if board[location] == 'x':
            b = board[:location] + 'W' + board[location + 1:]  # Create a new board string with a white piece added
            if closeMill(location, b):
                GenerateRemove(b, L)
            else:
                L.append(b)
    
    return L

def GenerateMovesOpening(board: str) -> list:
    """
    Generate new board positions for the opening phase by adding a white piece.

    Args:
        board (str): The current board position as a string.

    Returns:
        list: A list of new board positions.
    """
    return GenerateAdd(board)

def GenerateHopping(board: str) -> list:
    """
    Generate new board positions by hopping a white piece to any open spot.

    Args:
        board (str): The current board position as a string.

    Returns:
        list: A list of new board positions.
    """
    L = []

    for alpha in range(len(board)):
        if board[alpha] == 'W':
            for beta in range(len(board)):
                if board[beta] == 'x':
                    b = board[:alpha] + 'x' + board[alpha + 1:]  # Remove the white piece from alpha
                    b = b[:beta] + 'W' + b[beta + 1:]  # Place the white piece at beta
                    if closeMill(beta, b):
                        GenerateRemove(b, L)
                    else:
                        L.append(b)
    
    return L

def neighbors(j: int) -> list:
    """
    Get the list of neighbors for a given location on the board.

    Args:
        j (int): The index of the location on the board.

    Returns:
        list: A list of indices corresponding to the neighbors of the given location.
    """
    coord = indexToCoordDict[j]  # Translate index to coordinate
    neighbor_coords = neighborsDict[coord]  # Find neighbors using the coordinate
    neighbor_indices = [coordToIndexDict[n] for n in neighbor_coords]  # Translate neighbors back to indices
    return neighbor_indices

def GenerateMove(board: str) -> list:
    """
    Generate new board positions by moving white pieces to their neighboring empty spots.

    Args:
        board (str): The current board position as a string.

    Returns:
        list: A list of new board positions.
    """
    L = []

    for location in range(len(board)):
        if board[location] == 'W':
            n = neighbors(location)
            for j in n:
                if board[j] == 'x':
                    b = board[:location] + 'x' + board[location + 1:]  # Remove the white piece from the original location
                    b = b[:j] + 'W' + b[j + 1:]  # Place the white piece in the neighboring location
                    if closeMill(j, b):
                        GenerateRemove(b, L)
                    else:
                        L.append(b)
    
    return L

def GenerateMovesMidgameEndgame(board: str) -> list:
    """
    Generate new board positions for midgame or endgame by either hopping or moving white pieces.

    Args:
        board (str): The current board position as a string.

    Returns:
        list: A list of new board positions.
    """
    # Count the number of white pieces on the board
    white_pieces_count = board.count('W')

    if white_pieces_count < 3:
        #print("ERROR: Fewer than 3 pieces.")
        return []

    if white_pieces_count == 3:
        #print("3 white pieces - HOPPING")
        return GenerateHopping(board)
    else:
        #print("4+ white pieces - MOVING")
        return GenerateMove(board)
    
def SwapBlackWhite(board: str) -> str:
    """
    Swap white pieces to black and black pieces to white on the board.

    Args:
        board (str): The current board position as a string.

    Returns:
        str: The board position with white and black pieces swapped.
    """
    return board.replace('W', 'temp').replace('B', 'W').replace('temp', 'B')

def GenerateMovesOpeningBlack(board: str) -> list:
    """
    Generate new board positions for the opening phase by adding a black piece.

    Args:
        board (str): The current board position as a string.

    Returns:
        list: A list of new board positions.
    """
    swapped_board = SwapBlackWhite(board)
    new_positions = GenerateMovesOpening(swapped_board)
    return [SwapBlackWhite(pos) for pos in new_positions]

def GenerateMovesMidgameEndgameBlack(board: str) -> list:
    """
    Generate new board positions for midgame or endgame by either hopping or moving black pieces.

    Args:
        board (str): The current board position as a string.

    Returns:
        list: A list of new board positions.
    """
    swapped_board = SwapBlackWhite(board)
    new_positions = GenerateMovesMidgameEndgame(swapped_board)
    return [SwapBlackWhite(pos) for pos in new_positions]

def StaticEstMidgameEndgame(board: str) -> int:
    """
    Compute the static estimation for the midgame/endgame phase of the game.

    Args:
        board (str): The current board position as a string.

    Returns:
        int: The static estimation value.
    """
    numWhitePieces = board.count('W')
    numBlackPieces = board.count('B')
    L = GenerateMovesMidgameEndgameBlack(board)
    numBlackMoves = len(L)

    if numBlackPieces <= 2:
        return 10000
    elif numWhitePieces <= 2:
        return -10000
    elif numBlackMoves == 0:
        return 10000
    else:
        return 1000 * (numWhitePieces - numBlackPieces) - numBlackMoves
    
def StaticEstOpening(board: str) -> int:
    """
    Compute the static estimation for the opening phase of the game.

    Args:
        board (str): The current board position as a string.

    Returns:
        int: The static estimation value.
    """
    numWhitePieces = board.count('W')
    numBlackPieces = board.count('B')
    return numWhitePieces - numBlackPieces

def StaticEstMidgameEndgameBlack(board: str) -> int:
    """
    Compute the static estimation for the midgame/endgame phase of the game from Black's perspective.

    Args:
        board (str): The current board position as a string.

    Returns:
        int: The static estimation value.
    """
    numWhitePieces = board.count('W')
    numBlackPieces = board.count('B')
    L = GenerateMovesMidgameEndgame(board)
    numWhiteMoves = len(L)

    if numWhitePieces <= 2:
        return 10000
    elif numBlackPieces <= 2:
        return -10000
    elif numWhiteMoves == 0:
        return 10000
    else:
        return 1000 * (numBlackPieces - numWhitePieces) - numWhiteMoves
    
def StaticEstOpeningBlack(board: str) -> int:
    """
    Compute the static estimation for the opening phase of the game from Black's perspective.

    Args:
        board (str): The current board position as a string.

    Returns:
        int: The static estimation value.
    """
    numWhitePieces = board.count('W')
    numBlackPieces = board.count('B')
    return numBlackPieces - numWhitePieces