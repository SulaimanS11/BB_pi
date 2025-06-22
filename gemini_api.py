import google.generativeai as genai
import os
from danger_classes import dangerous_animals, dangerous_plants

def initialize_gemini():
    """Initialize Gemini API with API key"""
    # First try to import from ki.py
    try:
        from ki import ki
        API_KEY = ki
    except ImportError:
        # If ki.py doesn't exist, try environment variable
        API_KEY = os.environ.get('GEMINI_API_KEY')
        if not API_KEY:
            raise ValueError("No API key found. Please create ki.py with 'ki = \"your-api-key\"' or set GEMINI_API_KEY environment variable")
    
    genai.configure(api_key=API_KEY)
    return genai.GenerativeModel('gemini-1.5-flash')

def gemini_detect(model, pil_image):
    """Detect dangers in image using Gemini API"""
    try:
        # Craft a specific prompt for better detection
        prompt = """Analyze this image carefully for dangerous wildlife or plants.
        
        Look for:
        - Dangerous animals: bear, snake, wolf, wild boar, cougar, mountain lion, venomous spiders
        - Dangerous plants: poison ivy, poison oak, stinging nettle, giant hogweed
        
        If you detect any of these, respond with:
        1. The name of the danger
        2. Its position in the image (left, center, or right)
        
        Format: "[danger name] detected on the [position]"
        
        If no dangers are present, respond with "No dangers detected"
        
        Be specific and only identify if you're confident."""
        
        response = model.generate_content([prompt, pil_image])
        result = response.text.lower()
        
        print(f"Gemini response: {result}")  # Debug output
        
        # Parse response for dangers and positions
        positions = ["left", "center", "right"]
        all_dangers = list(dangerous_animals.keys()) + list(dangerous_plants.keys())
        
        for danger in all_dangers:
            if danger in result:
                for pos in positions:
                    if pos in result:
                        # Create approximate bounding box based on position
                        x_positions = {"left": 0.25, "center": 0.5, "right": 0.75}
                        x_center = x_positions.get(pos, 0.5)
                        
                        # Return danger and position info
                        bbox = (x_center - 0.15, 0.3, x_center + 0.15, 0.7)
                        return danger, bbox
        
        return None, None
        
    except Exception as e:
        print(f"Gemini detection error: {e}")
        return None, None