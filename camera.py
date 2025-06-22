from picamera2 import Picamera2
import numpy as np
from PIL import Image

class Camera:
    def __init__(self):
        self.picam2 = Picamera2()
        # Configure camera for still capture
        config = self.picam2.create_still_configuration(
            main={"size": (640, 480), "format": "RGB888"}
        )
        self.picam2.configure(config)
        self.picam2.start()

    def get_frame(self):
        try:
            # Capture array directly
            frame = self.picam2.capture_array()
            return frame
        except Exception as e:
            print(f"Error capturing frame: {e}")
            return None

    def get_pil_image(self):
        """Get PIL Image for Gemini API"""
        try:
            frame = self.picam2.capture_array()
            # Convert numpy array to PIL Image
            pil_image = Image.fromarray(frame)
            return pil_image
        except Exception as e:
            print(f"Error capturing PIL image: {e}")
            return None

    def release(self):
        self.picam2.stop()
        self.picam2.close()