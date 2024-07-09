# Function to perform the arithmetic operations
def arithmetic_operations(choice, num1, num2):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid choice."

# Read two numbers from the keyboard
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1/2/3/4): "))

result = arithmetic_operations(choice, num1, num2)
print("Result:", result)
