from picamera2 import Picamera2
import numpy as np
from PIL import Image
import time

class Camera:
    def __init__(self):
        try:
            self.camera = Picamera2()
            # Configure camera for still capture with lower resolution for faster processing
            config = self.camera.create_still_configuration(
                main={"size": (640, 480), "format": "RGB888"},
                buffer_count=1  # Reduce buffer count for lower memory usage
            )
            self.camera.configure(config)
            self.camera.start()
            # Allow camera to warm up
            time.sleep(2)
            print("Camera initialized successfully")
        except Exception as e:
            print(f"Failed to initialize camera: {e}")
            raise

    def get_frame(self):
        try:
            # Capture array directly
            frame = self.camera.capture_array()
            return frame
        except Exception as e:
            print(f"Error capturing frame: {e}")
            return None

    def get_pil_image(self):
        """Get PIL Image for Gemini API"""
        try:
            frame = self.camera.capture_array()
            # Convert numpy array to PIL Image
            pil_image = Image.fromarray(frame)
            return pil_image
        except Exception as e:
            print(f"Error capturing PIL image: {e}")
            return None

    def release(self):
        try:
            self.camera.stop()
            self.camera.close()
            print("Camera released")
        except:
            pass