from calibration import Calibration
from board_capture import BoardCapture

# Find the board
cal = Calibration()
corners = cal.find_corners()
homography_mtx = cal.get_homography_matrix(corners)

# Read the board
board = BoardCapture()
while True:
    input("Press enter to find board: ")
    new_board = board.get_board_array(homography_mtx)
    print(new_board)

