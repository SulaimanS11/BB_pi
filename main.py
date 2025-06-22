def main():
    print("Initializing Danger Detection System...")
    
    # Initialize components
    try:
        # Initialize Gemini
        print("Connecting to Gemini API...")
        model = initialize_gemini()
        
        # Initialize camera
        print("Initializing camera...")
        cam = Camera()
        
        # Initialize alert system
        print("Initializing alert system...")
        alert_system = AlertSystem()
        
    except Exception as e:
        print(f"Initialization failed: {e}")
        return
    
    print("\n✅ System ready! Monitoring for dangers...")
    print("Press Ctrl+C to stop\n")
    
    last_detection_time = 0
    detection_cooldown = 5  # Seconds between detections of same danger
    last_danger = None
    
    try:
        while True:
            # Get PIL image for Gemini API
            pil_image = cam.get_pil_image()
            if pil_image is None:
                time.sleep(1)
                continue

            # Get frame dimensions
            frame_width = pil_image.width
            frame_height = pil_image.height

            # Detect dangers using Gemini
            danger, bbox = gemini_detect(model, pil_image)

            if danger and bbox:
                # Check if we should alert (cooldown period)
                current_time = time.time()
                if danger != last_danger or (current_time - last_detection_time) > detection_cooldown:
                    # Calculate position
                    x_min, y_min, x_max, y_max = bbox
                    x_center = (x_min + x_max) / 2 * frame_width

                    direction = get_direction_from_bbox(x_center, frame_width)
                    action = get_safety_action(danger)
                    
                    # Alert the user
                    alert_system.alert_user(danger, direction, action)
                    
                    # Update detection tracking
                    last_detection_time = current_time
                    last_danger = danger
            else:
                # Reset last danger if nothing detected
                if time.time() - last_detection_time > detection_cooldown:
                    last_danger = None

            # Delay between checks (adjust based on your needs)
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\nShutting down system...")
    except Exception as e:
        print(f"\nError during operation: {e}")
    finally:
        cam.release()
        print("System shutdown complete.")


if __name__ == "__main__":
    main()