from PIL import Image
import pytesseract
from gtts import gTTS
import os

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def write_text_to_file(text, file_path):
    cleaned_text = ' '.join(text.split())
    with open(file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(cleaned_text)

def text_to_speech(text, file_path, language='en', slow=False):
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save(file_path)

if __name__ == '__main__':
    input_image_path = "Input_Images\\Book_1_left.jpg"
    output_folder_path = "Output"  

    # Process the input image
    extracted_text = extract_text_from_image(input_image_path)
    text_file_path = os.path.join(output_folder_path, "extracted_text.txt")
    write_text_to_file(extracted_text, text_file_path)

    # Convert extracted text to speech using gTTS
    output_audio_path = os.path.join(output_folder_path, "extracted_text.mp3")
    text_to_speech(extracted_text, output_audio_path)

    # Play the generated speech file
  #  os.system("start " + output_audio_path)  # On Windows
    # Add playback code for other platforms if needed
