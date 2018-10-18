def print_string_letter(word):
    "Using a for loop and range function, print out each letter of a given word"
    for letter in range(len(word)):
        print(word[letter])


# Question 9
"""Without using a builtin function, write a Python function to find a given 
character and return the first occurrence of the index."""
def return_character(character, phrase):
"""Return the index of the first occation of a chossen character."""

    for i in range(len(phrase)):
        if phrase[i] == character:
        return i





def main():

    word = "Python is Awesome"
    print_string_letter(word)

    # Question 9
    phrase = "Some bytes and byte array operations assume the use of ASCII compatible binary formats"
    character = "a"
    print(return_character(character, phrase))

main()