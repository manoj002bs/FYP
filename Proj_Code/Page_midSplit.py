from PIL import Image
import pytesseract
import os

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == '__main__':
    image_path = "Input_Images\\Book_1_right.jpg"
    extracted_text = extract_text_from_image(image_path)
    
    # Get the directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Specify the text file path in the same directory
    text_file_path = os.path.join(script_directory, "output_text.txt")
    
    # Write the extracted text to the text file
    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(extracted_text)
    
    print(f"Extracted Text has been written to: {text_file_path}")
