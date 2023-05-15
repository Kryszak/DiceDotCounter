import cv2


def create_detector():
    detector_parameters = cv2.SimpleBlobDetector_Params()
    detector_parameters.filterByConvexity = True
    detector_parameters.minConvexity = 0.9
    detector_parameters.filterByCircularity = 1
    detector_parameters.minCircularity = 0.9
    detector_parameters.maxThreshold = 100
    detector_parameters.filterByInertia = 1
    detector_parameters.minInertiaRatio = 0.6
    detector_parameters.filterByArea = 1
    detector_parameters.minArea = 200

    return cv2.SimpleBlobDetector_create(detector_parameters)


def process_frame(frame):
    frame_in_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold_frame = cv2.threshold(
        frame_in_grayscale, 100, 255, cv2.THRESH_BINARY)
    return threshold_frame


def main():
    video_capture = cv2.VideoCapture(0)

    if video_capture.isOpened():
        frame_available, frame = video_capture.read()
    else:
        frame_available = False

    detector = create_detector()

    while frame_available:
        processed_frame = process_frame(frame)
        keypoints = detector.detect(processed_frame)
        cv2.putText(frame, str(len(keypoints)), (0, 150),
                    cv2.FONT_HERSHEY_COMPLEX, 6, (0, 255, 0), 10)

        cv2.imshow("Dice dot counter", frame)
        frame_available, frame = video_capture.read()

        key = cv2.waitKey(20)
        if key == 27:
            break

    cv2.destroyWindow("preview")
    video_capture.release()


main()
