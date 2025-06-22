import pyttsx3

def alert_user(threat, direction, action):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Clear, moderate speech speed
    engine.setProperty('volume', 1.0)  # Maximum volume
    message = f"Warning: {threat} detected to your {direction}. {action}"
    print("Speaking alert:", message)
    engine.say(message)
    engine.runAndWait()
    engine.stop()
