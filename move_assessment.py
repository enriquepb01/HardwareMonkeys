from stockfish import Stockfish

init_array = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2]
]

test_array_e4 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2]
]

test_array_e4d5 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 0, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2]
]

test_array_e4d5xd5 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 0, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2]
]

def string_from_coords(coords):
    return chr(104 - coords[1]) + str(8 - coords[0])

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

print(move_from_arrays(init_array, test_array_e4))
print(move_from_arrays(test_array_e4, test_array_e4d5))
print(move_from_arrays(test_array_e4d5, test_array_e4d5xd5))




# stockfish = Stockfish(path="C:/Users/misha/Downloads/stockfish-windows-x86-64-avx2/stockfish/stockfish-windows-x86-64-avx2.exe")

# stockfish.update_engine_parameters( {"Hash": 512, "Threads": 3})

# stockfish.set_depth(22)

# stockfish.set_position(["e2e4"])

# print(stockfish.get_evaluation())

# stockfish.make_moves_from_current_position(["e7e5"])

# print(stockfish.get_evaluation())

# stockfish.make_moves_from_current_position(["d1h5"])

# print(stockfish.get_evaluation())

# stockfish.make_moves_from_current_position(["e8e7"])

# print(stockfish.get_evaluation())

# stockfish.make_moves_from_current_position(["h5e5"])

# print(stockfish.get_evaluation())