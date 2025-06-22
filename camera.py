"""
Danger Detection System using Raspberry Pi Camera and Google Gemini API
"""

import time
import sys
from pathlib import Path

# === camera.py ===
from picamera2 import Picamera2
import numpy as np
from PIL import Image

class Camera:
    def __init__(self):
        try:
            self.picam2 = Picamera2()
            # Configure camera for still capture with lower resolution for faster processing
            config = self.picam2.create_still_configuration(
                main={"size": (640, 480), "format": "RGB888"},
                buffer_count=1  # Reduce buffer count for lower memory usage
            )
            self.picam2.configure(config)
            self.picam2.start()
            # Allow camera to warm up
            time.sleep(2)
            print("Camera initialized successfully")
        except Exception as e:
            print(f"Failed to initialize camera: {e}")
            raise

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
        try:
            self.picam2.stop()
            self.picam2.close()
            print("Camera released")
        except:
            pass