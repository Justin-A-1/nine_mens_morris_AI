from building_blocks import *
from improved_static_est_parts import *

def StaticEstOpeningImproved(board: str, piece: str) -> int:
    """
    Compute the improved static estimation for the opening phase of the game.

    Args:
        board (str): The current board position as a string.
        piece (str): The piece type to evaluate for ('W' or 'B').

    Returns:
        int: The improved static estimation value.
    """
    numWhitePieces = board.count('W')
    numBlackPieces = board.count('B')
    numWhitePotentialMills = countPotentialMills(board, 'W')
    numBlackPotentialMills = countPotentialMills(board, 'B')
    numWhiteThreeMillPositions = countThreeMillPositions(board, 'W')
    numBlackThreeMillPositions = countThreeMillPositions(board, 'B')
    numWhiteOneMillPositions = countOneMillPositions(board, 'W')
    numBlackOneMillPositions = countOneMillPositions(board, 'B')
    numWhiteFourNeighborPositions = countFourNeighborPositions(board, 'W')
    numBlackFourNeighborPositions = countFourNeighborPositions(board, 'B')
    numWhiteBlockedPieces = countBlockedPieces(board, 'W')
    numBlackBlockedPieces = countBlockedPieces(board, 'B')

    score = (1000 * (numWhitePieces - numBlackPieces) +
             83 * numWhitePotentialMills - 82 * numBlackPotentialMills +
             27 * numWhiteThreeMillPositions - 26.9 * numBlackThreeMillPositions -
             26 * numWhiteOneMillPositions + 25.9 * numBlackOneMillPositions +
             4 * numWhiteFourNeighborPositions - 3.9 * numBlackFourNeighborPositions -
             0.24 * numWhiteBlockedPieces + 0.25 * numBlackBlockedPieces)

    if piece == 'W':
        return score
    elif piece == 'B':
        return -score

def MiniMaxOpeningImproved(board: str, depth: int, is_maximizing: bool):
    if depth == 0:
        return StaticEstOpeningImproved(board, 'W'), board, 1

    positions_evaluated = 0

    if is_maximizing:
        max_eval = float('-inf')
        best_board = None
        for child in GenerateMovesOpening(board):
            eval, _, child_positions_evaluated = MiniMaxOpeningImproved(child, depth - 1, False)
            positions_evaluated += child_positions_evaluated
            if eval > max_eval:
                max_eval = eval
                best_board = child
        return max_eval, best_board, positions_evaluated
    else:
        min_eval = float('inf')
        best_board = None
        for child in GenerateMovesOpeningBlack(board):
            eval, _, child_positions_evaluated = MiniMaxOpeningImproved(child, depth - 1, True)
            positions_evaluated += child_positions_evaluated
            if eval < min_eval:
                min_eval = eval
                best_board = child
        return min_eval, best_board, positions_evaluated

def main(input_file: str, output_file: str, depth: int):
    with open(input_file, 'r') as file:
        board = file.read().strip()

    eval, best_board, positions_evaluated = MiniMaxOpeningImproved(board, depth, True)

    with open(output_file, 'w') as file:
        file.write(best_board)

    print(f"Board Position: {best_board}")
    print(f"Positions evaluated by static estimation: {positions_evaluated}")
    print(f"MINIMAX-OPENING-IMPROVED estimate: {eval}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python MiniMaxOpeningImproved.py <input_file> <output_file> <depth>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        depth = int(sys.argv[3])
        main(input_file, output_file, depth)