# Mohamed Houqe
# Python Programming - Assignment 4
# Building Functions and Handling Errors Gracefully

import math


# This global variable can be read throughout the program.
result = 0


def convert_number(text):
    """Return text as a finite float, raising ValueError for invalid input."""
    number = float(text)
    if not math.isfinite(number):
        raise ValueError("Please enter a finite number.")
    return number


def add_numbers(first_number, second_number=0):
    """Return the sum of two numbers; the second number defaults to zero."""
    # This local result is separate from the global variable named result.
    result = first_number + second_number
    return result


def divide_numbers(dividend, divisor):
    """Return dividend divided by divisor, raising ZeroDivisionError for zero."""
    return dividend / divisor


if __name__ == "__main__":
    print("Welcome to my simple calculator!")

    # Repeat the prompts if either entry is not a valid number.
    while True:
        try:
            first_number = convert_number(input("Enter the first number: "))
            second_number = convert_number(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers such as 5 or 2.5.")

    sum_result = add_numbers(first_number, second_number)
    print(f"{first_number} + {second_number} = {sum_result}")

    # Calling the function with one argument uses its default parameter.
    default_result = add_numbers(first_number)
    print(f"Adding {first_number} with the default second number gives {default_result}.")

    print(f"The local result returned by add_numbers was {sum_result}.")
    print(f"The global result is still {result}, because local variables are separate.")

    try:
        quotient = divide_numbers(first_number, second_number)
        print(f"{first_number} / {second_number} = {quotient}")
    except ZeroDivisionError:
        print("Cannot divide by zero. The addition result is still available above.")

    print("Thanks for using my calculator!")
