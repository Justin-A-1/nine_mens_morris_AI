from building_blocks import *
from improved_static_est_parts import *
from ABGameImproved import ABGameImproved

def main(input_file: str, output_file: str, depth: int):
    with open(input_file, 'r') as file:
        board = file.read().strip()

    board = SwapBlackWhite(board)
    eval, best_board, positions_evaluated = ABGameImproved(board, depth, float('-inf'), float('inf'), True)
    best_board = SwapBlackWhite(best_board)

    with open(output_file, 'w') as file:
        file.write(best_board)

    print(f"Board Position: {best_board}")
    print(f"Positions evaluated by static estimation: {positions_evaluated}")
    print(f"AB-GAME-IMP-BLACK estimate: {eval}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python ABGameImpBlack.py <input_file> <output_file> <depth>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        depth = int(sys.argv[3])
        main(input_file, output_file, depth)