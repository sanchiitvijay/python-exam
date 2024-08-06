import re

def count_occurrences(text):
    vowels = re.findall(r'[aeiouAEIOU]', text)
    consonants = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text)
    digits = re.findall(r'\d', text)

    vowel_count = len(vowels)
    consonant_count = len(consonants)
    digit_count = len(digits)

    return vowel_count, consonant_count, digit_count

text = input("Enter a text: ")

vowels, consonants, digits = count_occurrences(text)

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
