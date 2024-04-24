import pyttsx3

def text_to_speech(file_path, rate=150):
    # Initialize the text-to-speech engine
    text_speech = pyttsx3.init()

    try:
        # Set the rate of speech
        text_speech.setProperty('rate', rate)

        # Open the text file
        with open(file_path, 'r', encoding='utf-8') as text_file:
            # Read the content of the file
            content = text_file.read()

            # Say the content
            text_speech.say(content)
            text_speech.runAndWait()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Specify the path of the text file to be read
    text_file_path = "output_text.txt"

    # Specify the rate (words per minute)
    speech_rate = 100

    # Call the function to convert text to speech with the specified rate
    text_to_speech(text_file_path, rate=speech_rate)
