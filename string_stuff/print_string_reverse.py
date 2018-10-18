def print_string_reversed_long(str):
    """ Given a string input, print that string in reverse without using special functions"""

    string_revered = ""

    for i in range(len(str), 0, -1):
       string_revered += str[i-1]

    return string_revered


def print_reversed_string_short(str):
    """Given a string input, use a shorthand method to reverse a string, return and print it"""

    return str[::-1]



def main():

    user_string_input = input("Please enter in a word to be printed in reverse:")
    print(print_string_reversed_long(user_string_input))

    print(print_reversed_string_short(user_string_input))

main()