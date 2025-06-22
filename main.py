import camera
import alerts
import danger_classes
import gemini_api
import utils.sensors as sensors
import time
import numpy as np

def main():
    cam = camera.Camera()
    print("Camera initialized. Starting danger detection...")
    
    try:
        while True:
            # Get PIL image for Gemini API
            pil_image = cam.get_pil_image()
            if pil_image is None:
                continue

            # Get frame dimensions for direction calculation
            frame_width = pil_image.width
            frame_height = pil_image.height

            # Detect dangers using Gemini
            danger, bbox = gemini_api.gemini_detect(pil_image)

            if danger and bbox:
                x_min, y_min, x_max, y_max = bbox
                x_center = (x_min + x_max) / 2 * frame_width

                direction = sensors.get_direction_from_bbox(x_center, frame_width)
                action = danger_classes.get_safety_action(danger)
                alerts.alert_user(danger, direction, action)
                
                # Wait a bit before next detection to avoid spam
                time.sleep(2)

            # Small delay to prevent excessive API calls
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        cam.release()

if __name__ == "__main__":
    main()