# Mohamed Houqe
# Python Programming - Assignment 4
# Building Functions and Handling Errors Gracefully

import math


# This variable is outside the functions, so it is global.
result = 0


def convert_number(text):
    """Turn text into a number. Raise ValueError if the input is invalid."""
    number = float(text)
    if not math.isfinite(number):
        raise ValueError("Please enter a finite number.")
    return number


def add_numbers(first_number, second_number=0):
    """Add two numbers and return the answer. The second number can be left out."""
    # This result is local, so it does not change the global result.
    result = first_number + second_number
    return result


def divide_numbers(dividend, divisor):
    """Divide two numbers and return the answer. Dividing by 0 raises ZeroDivisionError."""
    return dividend / divisor


if __name__ == "__main__":
    print("Welcome to my simple calculator!")

    # Ask again if the user does not enter a number.
    while True:
        try:
            first_number = convert_number(input("Enter the first number: "))
            second_number = convert_number(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers such as 5 or 2.5.")

    sum_result = add_numbers(first_number, second_number)
    print(f"{first_number} + {second_number} = {sum_result}")

    # Leave out the second number to use the default value of 0.
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
