"""Find averages and letter grades for main.py."""


def calculate_average(scores):
    """Return the average of a list of scores."""
    # main.py sends each student's scores to this function.
    if not scores:
        raise ValueError("The list of scores cannot be empty.")
    return sum(scores) / len(scores)


def get_letter_grade(score):
    """Return the letter grade for a score."""
    # main.py uses this function after finding the average.
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
