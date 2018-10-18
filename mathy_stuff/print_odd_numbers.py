def print_odd_nums(start, end):
    """ Print out odd numbers in a given range."""
    for i in range(start, end):
        if i %2 ==1:
           print(i, end = " ")


def print_odd_numbers_upgrade(start_num, end_num):
    """Print out odd numbers given a range of numbers by a user, 
    WITHOUT the range(), check for edgecase input issue, append numbers to a list."""

    if start_num > end_num:
        end_num, start_num = start_num, end_num

    else:
        start_num, end_num

    list_odd_nums = []

    while start_num < end_num:
        if start_num % 2 != 0:
            list_odd_nums.append(start)
        start_num += 1
    return list_odd_nums


def main():
    """Call functions here."""
    print_odd_nums(1, 23) 

    start_num = int(input("Give a start number: "))
    end_num = int(input("Give an end number: "))
    print(print_odd_numbers_upgrade(start_num, end_num))

main()