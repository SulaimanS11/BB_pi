import pyttsx3
import threading

class AlertSystem:
    def __init__(self):
        self.engine = None
        self.initialize_engine()
        
    def initialize_engine(self):
        try:
            self.engine = pyttsx3.init()
            # Configure voice properties
            self.engine.setProperty('rate', 150)  # Speech speed
            self.engine.setProperty('volume', 1.0)  # Maximum volume
            
            # Try to set a clearer voice if available
            voices = self.engine.getProperty('voices')
            if voices:
                self.engine.setProperty('voice', voices[0].id)
        except Exception as e:
            print(f"Failed to initialize TTS engine: {e}")
            self.engine = None

    def alert_user(self, threat, direction, action):
        """Alert user with voice and console output"""
        message = f"Warning: {threat} detected to your {direction}. {action}"
        
        # Always print to console
        print("\n" + "="*60)
        print(f"⚠️  DANGER ALERT ⚠️")
        print(f"Threat: {threat}")
        print(f"Direction: {direction}")
        print(f"Action: {action}")
        print("="*60 + "\n")
        
        # Try to speak the alert
        if self.engine:
            try:
                # Run TTS in a separate thread to avoid blocking
                tts_thread = threading.Thread(target=self._speak, args=(message,))
                tts_thread.daemon = True
                tts_thread.start()
            except Exception as e:
                print(f"TTS error: {e}")
        else:
            print("(TTS not available - alert shown in console only)")
    
    def _speak(self, message):
        """Internal method to speak message"""
        try:
            self.engine.say(message)
            self.engine.runAndWait()
        except:
            pass
