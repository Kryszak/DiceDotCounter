__author__ = 'olo & kryszak'
import numpy as np
import cv2
from matplotlib import pyplot as plt

fig = plt.figure()

def main():
    vc = cv2.VideoCapture(0)

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    while rval:

        imageGrey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(imageGrey, 100,255, cv2.THRESH_BINARY)

        params = cv2.SimpleBlobDetector_Params()

        params.filterByConvexity = True
        params.minConvexity = 0.9

        filterByCircularity = 1
        params.minCircularity = 0.9

        params.maxThreshold = 100

        params.filterByInertia = 1
        params.minInertiaRatio = 0.6

        params.filterByArea = 1
        params.minArea = 200

        detector = cv2.SimpleBlobDetector(params)
        keypoints = detector.detect(thresh)
        cv2.putText(frame, str(len(keypoints)), (0,150), cv2.FONT_HERSHEY_COMPLEX, 6, (0,255,0), 10)

        cv2.imshow("Dice dot counter",frame)
        rval, frame = vc.read()

        key = cv2.waitKey(20)
        if key == 27:
            break

    cv2.destroyWindow("preview")
    vc.release()
    np.set_printoptions(threshold='nan')

main()