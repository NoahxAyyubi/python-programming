# Mohamed Houqe
# Python Programming - Assignment 3
# Writing Programs with Decisions and Loops

print("Welcome to my decisions and loops program!")

# Use a for loop and conditions to show a letter grade for each score.
scores = [95, 84, 73, 62, 55]

print("\nStudent grade report:")
for score in scores:
    if score >= 90:
        letter_grade = "A"
    elif score >= 80:
        letter_grade = "B"
    elif score >= 70:
        letter_grade = "C"
    elif score >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print(f"A score of {score} earns a grade of {letter_grade}.")

# Keep asking for a guess until the user finds the secret number.
secret_number = "7"

print("\nGuess the secret number from 1 to 10.")
while True:
    guess = input("Enter your guess: ").strip()

    if guess == secret_number:
        print("Correct! You guessed the secret number.")
        break
    else:
        print("That is not the secret number. Try again.")

print("Thanks for using my program!")
