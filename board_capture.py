import numpy as np
import cv2
import matplotlib.pyplot as plt
from picamera.array import PiRGBArray
from picamera import PiCamera

class BoardCapture:
    def __init__(self):
        self.camera = PiCamera()
        self.rawCapture = PiRGBArray(self.camera)


    def get_board_array(self, homography_mtx):
        # ret, im = self.cap.read()
        self.camera.capture(self.rawCapture, format="rgb")
        im = self.rawCapture.array
        self.rawCapture.truncate(0)

        ## DEBUG ##
        # im = cv2.imread('test_board.jpg')
        ## END DEBUG ##

        # im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
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
                # plt.imshow(transformed_image[xmin:xmax, ymin:ymax])
                # plt.show()

                # check color of square and compare with red
                green_found = 0
                red_found = 0
                for row in transformed_image[xmin:xmax, ymin:ymax]:
                    for pixel in row:
                        if pixel[1] > pixel[0]+30 and pixel[1] > pixel[2]+30:
                            green_found += 1
                            
                        if pixel[0] > pixel[1]+50 and pixel[0] > pixel[2]+50:
                            red_found += 1
                        
                        if green_found > 9 or red_found > 9:
                            break
                            
                if green_found > 9:
                    chess_board.append(1)
                elif red_found > 9:
                    chess_board.append(2)
                else:
                    chess_board.append(0)

        chess_board = np.reshape(chess_board, (8,8))
        return chess_board
