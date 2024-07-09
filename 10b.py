def handle_exceptions():
    try:
        # NameError
        print(undefined_variable)

        # IndexError
        numbers = [1, 2, 3]
        print(numbers[5])

        # KeyError
        my_dict = {'a': 1, 'b': 2}
        print(my_dict['c'])

        # ZeroDivisionError
        result = 10 / 0
        print(result)

    except NameError as e:
        print(f"NameError occurred: {e}")
    except IndexError as e:
        print(f"IndexError occurred: {e}")
    except KeyError as e:
        print(f"KeyError occurred: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

handle_exceptions()
