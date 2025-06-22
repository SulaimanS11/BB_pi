dangerous_animals = {
    "bear": "Move away slowly, avoid direct eye contact, never run.",
    "snake": "Step back slowly, remain calm and avoid sudden movements.",
    "wolf": "Stand your ground, don't run, appear bigger and back away slowly.",
    "dog": "Avoid direct eye contact, stand still, and slowly back away.",
    "wild boar": "Back away slowly, find cover, do not run.",
    "cougar": "Face the animal, appear large, back away slowly, never run.",
    "mountain lion": "Face the animal, appear large, back away slowly, never run."
}

dangerous_plants = {
    "poison ivy": "Avoid touching. Move away and wash your skin immediately if contacted.",
    "poison oak": "Do not touch. Carefully move away and cleanse skin thoroughly if contacted.",
    "stinging nettle": "Avoid contact. If touched, wash with soap and cold water.",
    "giant hogweed": "Avoid all contact. Can cause severe burns. Seek medical help if touched."
}

def get_safety_action(label):
    # Normalize the label
    label_lower = label.lower().strip()
    
    # Check for partial matches in dangerous animals
    for animal, action in dangerous_animals.items():
        if animal in label_lower:
            return action
    
    # Check for partial matches in dangerous plants
    for plant, action in dangerous_plants.items():
        if plant in label_lower:
            return action
    
    # Default action
    return "Unidentified potential danger. Move cautiously away and maintain safe distance."
