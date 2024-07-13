from building_blocks import *

def ABGame(board: str, depth: int, alpha: float, beta: float, is_maximizing: bool):
    if (depth == 0 or (is_maximizing and not GenerateMovesMidgameEndgame(board)) or 
        (not is_maximizing and not GenerateMovesMidgameEndgameBlack(board))):
        return StaticEstMidgameEndgame(board), board, 1

    positions_evaluated = 0

    if is_maximizing:
        max_eval = float('-inf')
        best_board = None
        for child in GenerateMovesMidgameEndgame(board):
            eval, _, child_positions_evaluated = ABGame(child, depth - 1, alpha, beta, False)
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
        for child in GenerateMovesMidgameEndgameBlack(board):
            eval, _, child_positions_evaluated = ABGame(child, depth - 1, alpha, beta, True)
            positions_evaluated += child_positions_evaluated
            if eval < min_eval:
                min_eval = eval
                best_board = child
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_board, positions_evaluated

def main(input_file: str, output_file: str, depth: int):
    with open(input_file, 'r') as file:
        board = file.read().strip()

    eval, best_board, positions_evaluated = ABGame(board, depth, float('-inf'), float('inf'), True)

    with open(output_file, 'w') as file:
        file.write(best_board)

    print(f"Board Position: {best_board}")
    print(f"Positions evaluated by static estimation: {positions_evaluated}")
    print(f"ALPHA-BETA estimate: {eval}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python ABGame.py <input_file> <output_file> <depth>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        depth = int(sys.argv[3])
        main(input_file, output_file, depth)