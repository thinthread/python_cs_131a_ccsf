def sum_to_stop_num(stop_num):
    """ Return the sum of 1 + 2 +3 till you hit a given stop number such as n. """

    summed_up_nums = 0 # 1, 3 ,6, 10

    start_num = 1 # 2 , 3, 4, 5

    while start_num <= stop_num:
        summed_up_nums = summed_up_nums + start_num
        start_num = start_num + 1

    return summed_up_nums


def main():

    print(sum_to_stop_num(4))

main()