def get_direction_from_bbox(x_center, frame_width):
    """
    Determines relative direction based on object's x-coordinate in the frame.
    Args:
        x_center: Center X coordinate of detected object (bounding box).
        frame_width: Width of the camera frame.
    Returns:
        Direction as a string (e.g., "left", "center", "right").
    """
    third = frame_width / 3
    if x_center < third:
        return "left"
    elif x_center < 2 * third:
        return "center"
    else:
        return "right"