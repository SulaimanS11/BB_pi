import camera
import alerts
import danger_classes
import gemini_api
import utils.sensors as sensors
import cv2

def main():
    cam = camera.Camera()
    try:
        while True:
            frame = cam.get_frame()
            if frame is None:
                continue

            frame_height, frame_width = frame.shape[:2]

            danger, bbox = gemini_api.gemini_detect(frame)  # Update gemini_api.py to return bbox if possible

            if danger and bbox:
                x_min, y_min, x_max, y_max = bbox
                x_center = (x_min + x_max) / 2 * frame_width

                direction = sensors.get_direction_from_bbox(x_center, frame_width)
                action = danger_classes.get_safety_action(danger)
                alerts.alert_user(danger, direction, action)

            cv2.imshow("Danger Detector", frame)
            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()