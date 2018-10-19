# Question 12
def print_string_word(phrase):
    "Print out the word Programming from the given phrase"
    return phrase[7:]


# Question 13
def print_powers_2(n):
    """ Return the sum of squares of integers up to any given number of terms, 
    n as in 12 + 22 + 32 + .........+ n2, where n = 4"""
    sum_total = 0
    
    counter_num = 1
    
    while counter_num <= n:
        sum_total = sum_total + counter_num ** 2
        counter_num += 1
        
    return sum_total


# Question 14
def print_reversed_string(str):
    """Given a string input, use a shorthand method to reverse a string, return and print it"""

    return str[::-1]


# Quesiton 15
def is_secure_site(url):
    """ Given a URL, check whether this URL belongs to a secure site, eg:'https:'"""
    
    if url[0:6] == "https:":
        return "YAY,this site is secure!"
    else:
        return "Sorry, this is not a secure site... :-(("


def main():

    # Question 12
    phrase = "Python Programming"
    print(print_string_word(phrase))


    # Question 13
    print(print_powers_2(4))


    # Question 14
    print(print_reversed_string("Python"))

    # Question 15
    url_to_check = input("Please submit a url to check if it secure: ")
    print(is_secure_site(url_to_check))


main()


    