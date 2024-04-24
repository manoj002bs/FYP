from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == '__main__':
    image_path = "Input_Images\Book_1.jpg"
    output_file = "extracted_text.txt"

    extracted_text = extract_text_from_image(image_path)
    
    save_text_to_file(extracted_text, output_file)

    print("Extracted Text:\n")
    print(extracted_text)
    print(f"\nText saved to {output_file}")
