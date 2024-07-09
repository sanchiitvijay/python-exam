import random

def generate_random_numbers(count):
    return [random.randint(1, 100) for _ in range(count)]

def filter_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    odd_two_digit_numbers = [num for num in odd_numbers if 10 <= num <= 99]
    odd_four_digit_numbers = [num for num in odd_numbers if 1000 <= num <= 9999]
    return odd_two_digit_numbers, odd_four_digit_numbers

random_numbers = generate_random_numbers(20)
print("Generated Random Numbers:", random_numbers)

odd_two_digit_numbers, odd_four_digit_numbers = filter_odd_numbers(random_numbers)

print("\nOdd numbers of length 2:", odd_two_digit_numbers)
print("Odd numbers of length 4:", odd_four_digit_numbers)
