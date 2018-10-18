""" Write a Python function to print a geometric progression (Links to an external site.)
Links to an external#site. of a given first term (a)(start), common ratio (r)(stop) and number of terms(n)(step).

A geometric progression is a sequence of numbers where each term after the first is found by
multiplying the previous one by a fixed, non-zero number called the common ratio. 

Use your function to generate all the powers of 2 from 2 to 512 like in one 
line like 2, 4, 8,   ..... 512

"a" is the start number
"r" the stop number
"n" is the step by number

"""


def geo_progression_1(a, r, n):
    """ Prints a gemoteric series of numbers """

    term = a

    for i in range(1, n): # here n is how nth term
        print(term, end =", ")
        term *= r # Every term is r times the previous term


def geo_progression_2(a, r, end):
    """ Prints a gemoteric series of numbers """

    term = a

    while term <=512: # here end means the last or the nth term
        print(term, end =", ")
        term *= r


def main():

    geo_progression1(2, 2, 10)
    geo_progression2(2, 2, 512)

main()