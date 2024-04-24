def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_character_accuracy(ground_truth, recognized_text):
    total_characters = len(ground_truth)
    correct_characters = sum(gt == rec for gt, rec in zip(ground_truth, recognized_text))
    accuracy = correct_characters / total_characters * 1000
    return accuracy

def main():
    # Replace these with the paths to your ground truth and recognized text files
    ground_truth_path = 'original_text_2.txt'
    recognized_text_path = 'extracted_text_2.txt'

    # Read the texts from the files
    ground_truth = read_text_file(ground_truth_path)
    recognized_text = read_text_file(recognized_text_path)

    # Calculate and print the character accuracy
    accuracy = calculate_character_accuracy(ground_truth, recognized_text)
    print(f'Character Accuracy: {accuracy:.2f}%')

if __name__ == "__main__":
    main()
