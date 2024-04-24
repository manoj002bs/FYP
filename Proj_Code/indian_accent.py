import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for Indian English accent
engine.setProperty('voice', 'en-au')

# Set the speech rate (optional)
engine.setProperty('rate', 150)  # Adjust as needed

# Test the voice
engine.say("Hello, how are you?")
engine.runAndWait()
