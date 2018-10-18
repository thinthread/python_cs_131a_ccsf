def print_string_letter(word):
    "Using a for loop and range function, print out each letter of a given word"
    for letter in range(len(word)):
        print(word[letter])

def main():
    word = "Python is Awesome"
    print_string_letter(word)

main()