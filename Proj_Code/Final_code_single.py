from PIL import Image
import pytesseract
import pyttsx3
import os

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def write_text_to_file(text, file_path):
    cleaned_text = ' '.join(text.split())
    with open(file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(cleaned_text)

def text_to_speech(file_path, rate=150):
    text_speech = pyttsx3.init()
    text_speech.setProperty('voice', 'en-in')

    text_speech.setProperty('rate', rate)

    try:
        with open(file_path, 'r', encoding='utf-8') as text_file:
            content = text_file.read()
            text_speech.say(content)
            text_speech.runAndWait()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    input_image_path = "Input_Images\\Book_1_left.jpg"
    output_folder_path = "Output"  

    # Process the input image
    extracted_text = extract_text_from_image(input_image_path)
    text_file_path = os.path.join(output_folder_path, "extracted_text.txt")
    write_text_to_file(extracted_text, text_file_path)
    text_to_speech(text_file_path)
