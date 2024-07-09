def count_characters(filename):
    try:
        with open(filename, 'w') as file:
            print("Enter 5-6 lines of text:")
            for _ in range(5):
                line = input()
                file.write(line + '\n')

        with open(filename, 'r') as file:
            text = file.read()

        upper_count = sum(1 for char in text if char.isupper())
        lower_count = sum(1 for char in text if char.islower())
        digit_count = sum(1 for char in text if char.isdigit())

        print("\nDetails of the file:")
        print(f"Total characters: {len(text)}")
        print(f"Uppercase letters: {upper_count}")
        print(f"Lowercase letters: {lower_count}")
        print(f"Digits: {digit_count}")

    except IOError:
        print(f"Error: Could not read or write to file '{filename}'.")

filename = "user_text.txt"

count_characters(filename)
