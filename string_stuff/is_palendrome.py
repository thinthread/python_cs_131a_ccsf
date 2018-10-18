
def reverse_string(str): 
    # Reverse of a given string 
    return str[::-1] 

def is_palindrome(str): 
    # Call reverse function & check for equality
    rev = reverse_string(str) 

    if (str == rev): 
        return True 
    return False


def main():

    str = "racecar"
    check_palindrome = is_palindrome(str) 

    if check_palindrome == 1: 
        print("Yes") 
    else: 
        print("No")

main()