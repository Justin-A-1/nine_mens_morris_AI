from building_blocks import *
from improved_static_est_parts import *
from MiniMaxOpeningImproved import StaticEstOpeningImproved

def ABOpeningImproved(board: str, depth: int, alpha: float, beta: float, is_maximizing: bool):
    if depth == 0:
        return StaticEstOpeningImproved(board, 'W'), board, 1

    positions_evaluated = 0

    if is_maximizing:
        max_eval = float('-inf')
        best_board = None
        for child in GenerateMovesOpening(board):
            eval, _, child_positions_evaluated = ABOpeningImproved(child, depth - 1, alpha, beta, False)
            positions_evaluated += child_positions_evaluated
            if eval > max_eval:
                max_eval = eval
                best_board = child
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_board, positions_evaluated
    else:
        min_eval = float('inf')
        best_board = None
        for child in GenerateMovesOpeningBlack(board):
            eval, _, child_positions_evaluated = ABOpeningImproved(child, depth - 1, alpha, beta, True)
            positions_evaluated += child_positions_evaluated
            if eval < min_eval:
                min_eval = eval
                best_board = child
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_board, positions_evaluated