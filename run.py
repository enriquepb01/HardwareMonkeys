from calibration import Calibration
from board_capture import BoardCapture
from consts import init_array
from move_assessment import handle_eval, move_from_arrays
from stockfish import Stockfish

stockfish = Stockfish()
stockfish.update_engine_parameters( {"Hash": 512, "Threads": 3})

# Find the board
cal = Calibration()
corners = cal.find_corners()
homography_mtx = cal.get_homography_matrix(corners)

# Read the board
last_board = init_array
board = BoardCapture()
white_move = True
last_eval = {"type": "cp", "value": 0}
while True:
    input("Press enter after your move: ")
    new_board = board.get_board_array(homography_mtx)
    move_string = move_from_arrays(last_board, new_board)
    stockfish.make_moves_from_current_position([move_string])
    eval = stockfish.get_evaluation()

    if (white_move):
        handle_eval(eval, last_eval)

    white_move = not white_move
    last_board = new_board
    last_eval = eval
