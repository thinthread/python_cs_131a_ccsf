def str_rotation(word, n):
    """ Rotate a string with given amount of round clockwise """
    n = n % len(word) # With this this works for any amount of rounds even grater than the length
    return word[n:] + word[:n]


def main():

    print(str_rotation("Python", 4))

main()