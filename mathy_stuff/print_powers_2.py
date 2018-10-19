def print_powers_2(n):
    """ Return the sum of squares of integers up to any given number of terms, 
    n as in 12 + 22 + 32 + .........+ n2, where n = 4"""
    sum_total = 0
    
    counter_num = 1
    
    while counter_num <= n:
        sum_total = sum_total + counter_num ** 2
        counter_num += 1
        
    return sum_total


def main():
    print(print_powers_2(4))

main()