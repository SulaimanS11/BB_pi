# Install picamera2 (should be pre-installed on recent Raspberry Pi OS)
sudo apt update
sudo apt install python3-picamera2

# Install other requirements
pip3 install pyttsx3 google-generativeai numpy pillow

# If you need espeak for TTS on Pi
sudo apt install espeak espeak-data