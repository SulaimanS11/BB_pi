import google.generativeai as genai
from ki import ki

API_KEY = ki
genai.configure(api_key=API_KEY)

def gemini_detect(frame):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(["Identify dangerous animals or plants in this image, and state their positions clearly as 'left', 'center', or 'right'.", frame])
        result = response.text.lower()
        positions = ["left", "center", "right"]
        dangers = ["bear", "snake", "wolf", "poison ivy", "poison oak"]
        for danger in dangers:
            if danger in result:
                for pos in positions:
                    if pos in result:
                        # Return danger and approximate position based on Gemini description
                        x_center = {"left": 0.15, "center": 0.5, "right": 0.85}[pos]
                        bbox = (x_center - 0.05, 0, x_center + 0.05, 1)  # Mock bounding-box
                        return danger, bbox
        return None, None
    except Exception as e:
        print(f"Gemini detection error: {e}")
        return None, None