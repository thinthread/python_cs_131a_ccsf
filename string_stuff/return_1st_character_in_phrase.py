def return_character(character, phrase):
"""Return the index of the first occation of a chossen character."""

    for i in range(len(phrase)):
        if phrase[i] == character:
        return i


def main():

    phrase = "Some bytes and byte array operations assume the use of ASCII compatible binary formats"

    character = "a"

    print(return_character(character, phrase))

main()