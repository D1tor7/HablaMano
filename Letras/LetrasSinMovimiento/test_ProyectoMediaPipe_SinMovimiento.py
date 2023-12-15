import unittest
import cv2
from ProyectoMediaPipe_SinMovimiento import draw_landmarks_on_image, Detection
class TestDrawLandmarksOnImage(unittest.TestCase):
    def test_draw_landmarks_on_image(self):
        # Load the image for testing
        image_path = 'a.jpeg'
        image = cv2.imread(image_path)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Simulate a detection result (replace with actual detection result)
        hand_landmarks_list = [[landmark_pb2.NormalizedLandmark(x=0.1, y=0.1, z=0.1)]]
        handedness_list = [vision.Handedness(category_name="Left")]
        detection_result = Detection(hand_landmarks=hand_landmarks_list, handedness=handedness_list)

        # Call the function
        annotated_image = draw_landmarks_on_image(rgb_image, detection_result)

        # Ensure the output image is not None
        self.assertIsNotNone(annotated_image)

        # Optionally, you can save the output image for manual inspection
        cv2.imwrite('output_image.jpg', cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))

if __name__ == '__main__':
    unittest.main()