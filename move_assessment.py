from consts import MoveType, init_array
from stockfish import Stockfish

def string_from_coords(coords):
    return chr(104 - coords[0]) + str(8 - coords[1])

def move_from_arrays(prev_arr, post_arr):
    orig_posit = None
    dest_posit = None
    for i in range(8):
        for j in range(8):
            if prev_arr[i][j] != post_arr[i][j]:
                if (post_arr[i][j] == 0):
                    orig_posit = [i, j]
                else:
                    dest_posit = [i, j]
    return string_from_coords(orig_posit) + string_from_coords(dest_posit)

def handle_move_type(move_type):
    if (move_type == MoveType.GOOD):
        print("Good move")
    elif (move_type == MoveType.BAD):
        print("Bad move")
    elif (move_type == MoveType.NEUTRAL):
        print("Neutral move")
    elif (move_type == MoveType.CHECKMATE):
        print("Checkmate!")
        exit()

# Determine if the change since the last evaluation was good, bad, or neutral, and dispatch the appropriate action
def handle_eval(eval, last_eval):
    if (eval["type"] == "cp" and last_eval["type"] == "cp"):
        if (eval["value"] - last_eval["value"]  > 50): handle_move_type(MoveType.GOOD)
        elif (eval["value"] - last_eval["value"]  < -50): handle_move_type(MoveType.BAD)
        else: handle_move_type(MoveType.NEUTRAL)
    elif (eval["type"] == "mate" and eval["value"] == 0): handle_move_type(MoveType.CHECKMATE)
    elif (eval["type"] == "mate" and last_eval["type"] == "mate"):
        if (eval["value"] < last_eval["value"]): handle_move_type(MoveType.GOOD)
        else: handle_move_type(MoveType.BAD)
    elif (eval["type"] == "cp" and last_eval["type"] == "mate"): handle_move_type(MoveType.BAD)
    else: handle_move_type(MoveType.GOOD)