def add_entry(dictionary):
    word = input("Enter the word: ")
    meaning = input("Enter the meaning: ")
    dictionary[word] = meaning
    print(f"Entry added: {word}: {meaning}")

def search_word(dictionary):
    word = input("Enter the word to search: ")
    if word in dictionary:
        print(f"Meaning of '{word}': {dictionary[word]}")
    else:
        print(f"'{word}' not found in dictionary.")

def find_words_with_meaning(dictionary):
    meaning = input("Enter the meaning to search for words: ")
    words = [word for word, mean in dictionary.items() if mean == meaning]
    if words:
        print(f"Words with meaning '{meaning}': {', '.join(words)}")
    else:
        print(f"No words found with meaning '{meaning}'.")

def remove_entry(dictionary):
    word = input("Enter the word to remove: ")
    if word in dictionary:
        del dictionary[word]
        print(f"'{word}' removed from dictionary.")
    else:
        print(f"'{word}' not found in dictionary.")

def display_sorted(dictionary):
    sorted_words = sorted(dictionary.items())
    print("Dictionary sorted alphabetically:")
    for word, meaning in sorted_words:
        print(f"{word}: {meaning}")

dictionary = {}

while True:
    print("\nMenu:")
    print("1. Add new entry")
    print("2. Search for a word")
    print("3. Find words with the same meaning")
    print("4. Remove an entry")
    print("5. Display all words sorted alphabetically")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_entry(dictionary)
    elif choice == '2':
        search_word(dictionary)
    elif choice == '3':
        find_words_with_meaning(dictionary)
    elif choice == '4':
        remove_entry(dictionary)
    elif choice == '5':
        display_sorted(dictionary)
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
