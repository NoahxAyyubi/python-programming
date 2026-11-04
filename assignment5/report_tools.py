"""Put student results into readable text for main.py."""


def format_student_report(name, average, letter_grade):
    """Return one line with the student's name, average, and grade."""
    # main.py prints the text returned by this function.
    return f"{name}: average = {average:.1f}, grade = {letter_grade}"
