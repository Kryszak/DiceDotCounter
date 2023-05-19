import unittest
from counter.main import count_dice_dots, create_detector
import cv2


class TestDiceDotDetection(unittest.TestCase):
    def test_detect_dots_from_file(self):
        # given
        test_frame = cv2.imread('tests/test_frame.png')
        detector = create_detector()

        # when
        dot_count = count_dice_dots(test_frame, detector)

        # then
        self.assertEqual(dot_count, 4)


if __name__ == '__main__':
    unittest.main()
