"""
Main entry point for the Danger Detection System
"""

import time
import sys

# Import our modules
from camera import Camera
from alerts import AlertSystem
from gemini_api import initialize_gemini, gemini_detect
from danger_classes import get_safety_action
from utils.sensors import get_direction_from_bbox


def main():
    """Main program loop"""
    print("="*60)
    print("Danger Detection System v1.0")
    print("="*60)
    print("\nInitializing components...")
    
    # Initialize all components
    cam = None
    model = None
    alert_system = None
    
    try:
        # 1. Initialize Gemini API
        print("→ Connecting to Gemini API...")
        model = initialize_gemini()
        print("✓ Gemini API connected")
        
        # 2. Initialize camera
        print("→ Starting camera...")
        cam = Camera()
        print("✓ Camera ready")
        
        # 3. Initialize alert system
        print("→ Setting up alert system...")
        alert_system = AlertSystem()
        print("✓ Alert system ready")
        
    except Exception as e:
        print(f"\n❌ Initialization failed: {e}")
        print("\nTroubleshooting:")
        print("- Check your API key in ki.py")
        print("- Ensure camera is connected")
        print("- Verify internet connection")
        if cam:
            cam.release()
        sys.exit(1)
    
    print("\n" + "="*60)
    print("✅ SYSTEM READY - Monitoring for dangers")
    print("Press Ctrl+C to stop")
    print("="*60 + "\n")
    
    # Detection state tracking
    last_detection_time = 0
    detection_cooldown = 5  # Seconds between repeat alerts
    last_danger = None
    frame_count = 0
    
    try:
        while True:
            frame_count += 1
            
            # Capture image from camera
            pil_image = cam.get_pil_image()
            if pil_image is None:
                print(f"Warning: Failed to capture frame {frame_count}")
                time.sleep(1)
                continue
            
            # Show periodic status
            if frame_count % 30 == 0:  # Every ~30 seconds
                print(f"Status: Processed {frame_count} frames, system running...")
            
            # Send to Gemini for analysis
            danger, bbox = gemini_detect(model, pil_image)
            
            if danger and bbox:
                current_time = time.time()
                
                # Check if we should alert (avoid spam)
                should_alert = (danger != last_danger or 
                              (current_time - last_detection_time) > detection_cooldown)
                
                if should_alert:
                    # Extract position info
                    x_min, y_min, x_max, y_max = bbox
                    x_center = (x_min + x_max) / 2
                    
                    # Convert to pixel coordinates
                    x_center_pixels = x_center * pil_image.width
                    
                    # Get direction and safety action
                    direction = get_direction_from_bbox(x_center_pixels, pil_image.width)
                    action = get_safety_action(danger)
                    
                    # Alert the user
                    alert_system.alert_user(danger, direction, action)
                    
                    # Update tracking
                    last_detection_time = current_time
                    last_danger = danger
                    
                    print(f"[Frame {frame_count}] Detection logged")
            
            else:
                # Clear last danger after cooldown expires
                if time.time() - last_detection_time > detection_cooldown * 2:
                    last_danger = None
            
            # Rate limiting to avoid API spam
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n→ Shutdown requested...")
        
    except Exception as e:
        print(f"\n❌ Runtime error: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Clean shutdown
        print("→ Releasing resources...")
        if cam:
            cam.release()
        print("✓ System shutdown complete")
        print("\nThank you for using Danger Detection System!")


if __name__ == "__main__":
    main()