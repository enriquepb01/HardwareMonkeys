import numpy as np
import cv2
import cv2.aruco as aruco
import matplotlib.pyplot as plt

class Calibration:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    
    def find_corners(self):
        ret, im = self.cap.read()

        ## DEBUG ##
        im = cv2.imread('test_board.jpg')
        ## END DEBUG ##

        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # find Aruco markers
        dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
        parameters =  aruco.DetectorParameters()
        detector = aruco.ArucoDetector(dictionary, parameters)
        corners, ids, rejectedImgPoints = detector.detectMarkers(gray)
        points = []
        if ids is not None:
            for i in range(len(ids)):
                point_x = int(corners[i][0][0][0])
                point_y = int(corners[i][0][0][1])
                points.append((point_x, point_y, ids[i][0]))

        points = np.array(points)
        points = sorted(points, key = lambda x: x[2])
        points = [points[2], points[3], points[0], points[1]]

        ## DEBUG ##
        # print("Points: ",  points)
        # plt.imshow(gray, cmap='gray')
        # plt.show()
        ## END DEBUG ##

        return points

    def get_homography_matrix(self, corner_pixels):
        # create a matrix that translates 8x8 board into pixels
        A = []
        p2 = [[0,0],[0,800],[800,0],[800,800]]
        p1 = corner_pixels
        for i in range(4):
            x, y = p1[i][0], p1[i][1]
            u, v = p2[i][0], p2[i][1]
            A.append([x, y, 1, 0, 0, 0, -u * x, -u * y, -u])
            A.append([0, 0, 0, x, y, 1, -v * x, -v * y, -v])
        A = np.asarray(A)
        U, S, Vh = np.linalg.svd(A)
        L = Vh[-1, :] / Vh[-1, -1]
        H = L.reshape(3, 3)
        homography_mtx = H
        return homography_mtx
    
