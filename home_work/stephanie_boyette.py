# Question 14
def print_triangular_numbers():    
    """ Print triangular numbers from range 0-50, sequentially."""

    triangular_number = 0

    print("Question 14 - Sequence of 'Triangular Number' range 0-50:")

    for i in range(50):
        triangular_number = triangular_number + i
    
        print(triangular_number, end = ' ')


# Question 15
def turtle_draw_stairs(alexa, steps):
    """Draw a stair-case 20 steps in length using Python - Turtle."""

    number_of_steps = range(steps)

    for i in number_of_steps:
        alexa.left(90)
        alexa.forward(5)
        alexa.right(90)
        alexa.forward(10)
    print("\nTurtle stairway to heaven completed... yay!!!")


# Question 16
def count_digits():
    """Count the number of digit in number_to_count, no str() conversion."""
    
    total_digit_count = 0

    number_to_count = 1234554321 

    while (number_to_count > 0):
        number_to_count = number_to_count//10
        total_digit_count = total_digit_count + 1

    print ("Question 16\nTotal number of digits: ", total_digit_count)


# Question - 17 (Extra Credit)
def convert_num_binary(number_to_convert):
    """Convert any given number to binary."""
    
    current_power = 0

    binary_number = 0

    while number_to_convert > 0:
        binary_number = binary_number + 10 ** current_power * (number_to_convert % 2)
        number_to_convert = number_to_convert // 2
        current_power = current_power + 1

    print("Your number converted to binary is: ", binary_number)


def main():
    """Call functions and related statements in main()."""

    # Question 14
    print_triangular_numbers()
    print('\n')

    # Qestion 15
    import time
    for i in range(1):
        print("Question 15\n*** Note - Python Turtle function 'turtle_draw_stairs' will commence in 15 seconds.***")
        print("To exit the Python Turtle screen, click on the Turle sand-box when drawing is complete.")
        print("This will allow the rest of the code in this module to execute...\nHappy code viewing!")
        time.sleep(15)

    import turtle             
    screen = turtle.Screen()
    alexa = turtle.Turtle()
    turtle_draw_stairs(alexa, 20)
    screen.exitonclick() 
    print('\n')

    # Question 16
    count_digits()
    print('\n')      

    # Question - 17 (Extra Credit)
    convert_num_binary(int(input("Qestion - 17 (Extra credit)\nPlease enter in a number to be converted to binary: ")))
    print('\n')

main()