from building_blocks import *

def MiniMaxOpening(board: str, depth: int, is_maximizing: bool):
    if depth == 0:
        return StaticEstOpening(board), board, 1

    positions_evaluated = 0

    if is_maximizing:
        max_eval = float('-inf')
        best_board = None
        for child in GenerateMovesOpening(board):
            eval, _, child_positions_evaluated = MiniMaxOpening(child, depth - 1, False)
            positions_evaluated += child_positions_evaluated
            if eval > max_eval:
                max_eval = eval
                best_board = child
        return max_eval, best_board, positions_evaluated
    else:
        min_eval = float('inf')
        best_board = None
        for child in GenerateMovesOpeningBlack(board):
            eval, _, child_positions_evaluated = MiniMaxOpening(child, depth - 1, True)
            positions_evaluated += child_positions_evaluated
            if eval < min_eval:
                min_eval = eval
                best_board = child
        return min_eval, best_board, positions_evaluated

def main(input_file: str, output_file: str, depth: int):
    with open(input_file, 'r') as file:
        board = file.read().strip()

    eval, best_board, positions_evaluated = MiniMaxOpening(board, depth, True)

    with open(output_file, 'w') as file:
        file.write(best_board)

    print(f"Board Position: {best_board}")
    print(f"Positions evaluated by static estimation: {positions_evaluated}")
    print(f"MINIMAX estimate: {eval}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python MiniMaxOpening.py <input_file> <output_file> <depth>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        depth = int(sys.argv[3])
        main(input_file, output_file, depth)