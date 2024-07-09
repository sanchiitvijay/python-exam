def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Unsupported operation with types provided!")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Result of division: {result}")
    finally:
        print("Division operation completed.\n")

print("Test Case 1:")
divide_numbers(10, 2)

print("Test Case 2:")
divide_numbers(10, 0)

print("Test Case 3:")
divide_numbers(10, '2')
