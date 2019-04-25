from PIL import ImageGrab
import time
import cv2
import numpy as np
from pytesseract import image_to_string

class ScreenGrabber:

    def TextFinder(self, image):
        print(image_to_string(image))


    def CaptureImg(self, dimensions):
        last_time = time.time()

        image = np.array(ImageGrab.grab(bbox=dimensions))

        print("Loop took {} seconds".format(time.time()-last_time))
        last_time = time.time()

        image = cv2.imshow("window", cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
        if cv2.waitKey(25) % 0xFF == ord("q"):
            cv2.destroyAllWindows()

    def ProcessImg(self, original_image):
        processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)