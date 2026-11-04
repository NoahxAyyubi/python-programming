"""Run a student grade report using grade_tools and report_tools."""

# Mohamed Houqe
# Python Programming - Assignment 5

from datetime import date

# Import the whole grade_tools module.
import grade_tools

# Import just the function needed to format the report.
from report_tools import format_student_report


def main():
    """Use the two modules to show each student's average and grade."""
    students = {
        "Mohamed": [90, 85, 95],
        "Sara": [80, 75, 85],
        "Ali": [70, 65, 75],
    }

    print("Student Grade Report")
    print(f"Date: {date.today()}")
    print()

    for name, scores in students.items():
        average = grade_tools.calculate_average(scores)
        letter_grade = grade_tools.get_letter_grade(average)
        report = format_student_report(name, average, letter_grade)
        print(report)


if __name__ == "__main__":
    main()
