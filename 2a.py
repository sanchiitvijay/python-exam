def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

prime_numbers = prime_numbers_in_range(start, end)
print("Prime numbers in the range:", prime_numbers)
