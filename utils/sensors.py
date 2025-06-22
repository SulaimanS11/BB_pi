import smbus2
import math

def read_compass():
    # Replace this function with actual sensor reading logic
    # Example placeholder returning a fixed heading (in degrees)
    heading_degrees = 90  # East
    return heading_degrees

def get_direction():
    heading_degrees = read_compass()
    directions = ["North", "North-East", "East", "South-East",
                  "South", "South-West", "West", "North-West"]
    idx = round(heading_degrees / 45) % 8
    return directions[idx]
