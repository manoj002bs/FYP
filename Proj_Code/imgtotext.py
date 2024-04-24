from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def write_text_to_file(text, file_path):
    # Remove unnecessary newlines from the text
    cleaned_text = ' '.join(text.split())

    # Write the cleaned text to the text file
    with open(file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(cleaned_text)

if __name__ == '__main__':
    image_path = "Input_Images\Book_1_left.jpg"
    extracted_text = extract_text_from_image(image_path)
    
    # Specify the text file path
    text_file_path = "output_text.txt"
    
    # Write the extracted text (cleaned) to the text file
    write_text_to_file(extracted_text, text_file_path)
    
    print(f"Extracted Text has been written to: {text_file_path}")
