def is_num_even(number):
    """"Check to see if a given number is odd or even."""

    if number % 2:
        print("Your number is even!")
    else:
        print("Your number is not even... soooo sad :-( ...")


def main():
    """Call functions here."""

    is_num_even(input("Please enter in a number to check if it is!: "))

main()