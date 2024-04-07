import numpy as np
import cv2
import matplotlib.pyplot as plt

class BoardCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_board_array(self, homography_mtx):
        # ret, im = self.cap.read()

        ## DEBUG ##
        im = cv2.imread('test_board.jpg')
        ## END DEBUG ##

        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        # plt.imshow(im)
        # plt.show()

        transformed_image = cv2.warpPerspective(im, homography_mtx, (800, 800))
        # plt.imshow(transformed_image)
        # plt.show()

        # return chess array with 0 (no piece), 1 (white piece), 2 (black piece)
        chess_board = []
        for i in range(0, 701, 100):
            for j in range(0, 701, 100):
                xmin = i
                xmax = i+100
                ymin = j
                ymax = j+100
                plt.imshow(transformed_image[xmin:xmax, ymin:ymax])
                plt.show()

                # check color of square and compare with red
                color_found = 0
                for row in transformed_image[xmin:xmax, ymin:ymax]:
                    for pixel in row:
                        if pixel[1] > pixel[0]+30 and pixel[1] > pixel[2]+30:
                            color_found = 1
                            break
                        if pixel[0] > pixel[1]+30 and pixel[0] > pixel[2]+30:
                            color_found = 2
                            break
                    if color_found:
                        break

                chess_board.append(color_found)

        chess_board = np.reshape(chess_board, (8,8))
        return chess_board
