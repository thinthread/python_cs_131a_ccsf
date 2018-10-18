def calculate_letter_grade(number_score):
"""Calculate letter grade based on student test score."""

    if number_score >= 90:
        print("A")
    elif number_score >= 80 and number_score <90:
        print("B")
    elif number_score >= 65 and number_score <80:
        print("C")
    elif number_score >= 50 and number_score <65:
        print("D")
    else:
        print("F")


def main():

    calculate_letter_grade(88)

main()