def print_odd_nums(start, end):
    """ Print out odd numbers in a given range."""
    for i in range(start, end):
        if i %2 ==1:
           print(i, end = " ")



def main():
    """Call functions here."""
    print_odd_nums(1, 23) 

main()