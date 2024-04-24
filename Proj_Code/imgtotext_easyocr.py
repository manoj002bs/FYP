import easyocr

def perform_ocr(image_path):
    # Create an OCR reader
    reader = easyocr.Reader(['en'])

    # Perform OCR on the image
    result = reader.readtext(image_path)

    # Extract and print the text
    extracted_text = [entry[1] for entry in result]
    print("Extracted Text:\n")
    print("\n".join(extracted_text))

if __name__ == '__main__':
    image_path = "Input_Images\Book_1_left.jpg"
    perform_ocr(image_path)
