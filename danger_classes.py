dangerous_animals = {
    "bear": "Move away slowly, avoid direct eye contact, never run.",
    "snake": "Step back slowly, remain calm and avoid sudden movements.",
    "wolf": "Stand your ground, don't run, appear bigger and back away slowly."
}

dangerous_plants = {
    "poison ivy": "Avoid touching. Move away and wash your skin immediately.",
    "poison oak": "Do not touch. Carefully move away and cleanse skin thoroughly."
}

def get_safety_action(label):
    if label.lower() in dangerous_animals:
        return dangerous_animals[label.lower()]
    elif label.lower() in dangerous_plants:
        return dangerous_plants[label.lower()]
    else:
        return "Move cautiously away."
