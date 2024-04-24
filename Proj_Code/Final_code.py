from PIL import Image
import pytesseract
import pyttsx3
import os

def split_book_pages(image_path, output_folder_path):
    original_image = Image.open(image_path)
    width, height = original_image.size
    centerline = width // 2

    left_page = original_image.crop((0, 0, centerline, height))
    right_page = original_image.crop((centerline, 0, width, height))

    left_page.save(os.path.join(output_folder_path, "left_page.png"))
    right_page.save(os.path.join(output_folder_path, "right_page.png"))

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
    text_speech.setProperty('rate', rate)

    try:
        with open(file_path, 'r', encoding='utf-8') as text_file:
            content = text_file.read()
            text_speech.say(content)
            text_speech.runAndWait()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    input_image_path = "Input_Images\Book_1.jpg"
    output_folder_path = "Output"

    # Split the input image into left and right pages
    split_book_pages(input_image_path, output_folder_path)

    # Process the left page
    left_page_path = os.path.join(output_folder_path, "left_page.png")
    left_text_path = os.path.join(output_folder_path, "left_text.txt")
    extracted_left_text = extract_text_from_image(left_page_path)
    write_text_to_file(extracted_left_text, left_text_path)
    text_to_speech(left_text_path)

    # Process the right page
    right_page_path = os.path.join(output_folder_path, "right_page.png")
    right_text_path = os.path.join(output_folder_path, "right_text.txt")
    extracted_right_text = extract_text_from_image(right_page_path)
    write_text_to_file(extracted_right_text, right_text_path)
    text_to_speech(right_text_path)
