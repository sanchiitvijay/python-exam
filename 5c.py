def longest_and_shortest_words(filename):
    try:
        with open(filename, 'w') as file:
            print("Enter 5-6 lines of text:")
            for _ in range(5):
                line = input()
                file.write(line + '\n')

        with open(filename, 'r') as file:
            text = file.read()

        words = text.split()

        if not words:
            print("No words found in the file.")
            return

        longest_word = max(words, key=len)
        shortest_word = min(words, key=len)

        print("\nLongest word:", longest_word)
        print("Length of longest word:", len(longest_word))
        print("\nShortest word:", shortest_word)
        print("Length of shortest word:", len(shortest_word))

    except IOError:
        print(f"Error: Could not read or write to file '{filename}'.")

filename = "user_text.txt"

longest_and_shortest_words(filename)
