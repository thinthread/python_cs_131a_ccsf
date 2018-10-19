# Question 12
def toss_dice(number_of_sides):
    "Roll any polygon shape dice and return the rolled value."
    
    import random

    number_of_sides = tidy_user_input((number_of_sides))
    
    for i in number_of_sides:
        number_of_sides = int(number_of_sides)
        if number_of_sides >= 4:
            dice_face_showing = random.randrange(1, number_of_sides)
            print("Side facing up: ", dice_face_showing)

            repeat_dice_toss = input("If you would like to try again enter 'y' for yes. \nOr, you can hit any other key if you wish to exit toss_dice mode and move on with the next program: ")
            print("")
            
            if repeat_dice_toss == "y":
                dice_face_showing = random.randrange(1, number_of_sides)
                message = ("Dice roll in action... new side of dice facing up: ", dice_face_showing)
                return message

        else:
            number_of_sides = (input("Oops, a dice must have four or more sides, please try again: "))
            return toss_dice(number_of_sides)

# Question 13 - 1
def turtle_draw_numbers(alexa, cleaned_input):
    """Draw seven-segment-indicator numbers given user input, making calls to helper functions for each line segment."""
    
    print("Your number to be drawn: ", cleaned_input)

    for i in cleaned_input:
        if i == "0":
            make_line_a(alexa)
            make_line_b(alexa)
            make_line_c(alexa)
            make_line_d(alexa)
            make_line_e(alexa)
            make_line_f(alexa)
            space_between_numbers(alexa)

        if i == "1":
            alexa.penup()
            alexa.forward(2)
            alexa.pendown()
            alexa.forward(18)
            alexa.penup()
            alexa.forward(2)
            make_line_b(alexa)
            make_line_c(alexa)
            alexa.left(90)
            alexa.forward(2)
            alexa.forward(20)
            alexa.right(180)
            alexa.pendown()
            alexa.forward(41)
            alexa.forward(2)
            alexa.right(90)
            forward_2_then_45_(alexa)
            forward_2_then_45_(alexa)
            space_between_numbers(alexa)

        if i == "2":
            make_line_a(alexa)
            make_line_b(alexa)
            forward_2_then_45_(alexa)
            make_line_d(alexa)
            make_line_e(alexa)
            forward_2_then_45_(alexa)
            make_line_g(alexa)
            move_turle_zero_position(alexa)
            space_between_numbers(alexa)
            
        if i == "3":
            make_line_a(alexa)
            make_line_b(alexa)
            make_line_c(alexa)
            make_line_d(alexa)
            alexa.right(90)
            forward_2_then_45_(alexa)
            forward_2_then_45_(alexa)
            make_line_g(alexa)
            move_turle_zero_position(alexa)
            space_between_numbers(alexa)

        if i == "4":
            forward_2_then_45_(alexa)
            make_line_b(alexa)
            make_line_c(alexa)
            alexa.right(90)
            forward_2_then_45_(alexa)
            alexa.right(90)
            forward_2_then_45_(alexa)
            make_line_f(alexa)
            make_line_g(alexa)
            move_turle_zero_position(alexa)
            space_between_numbers(alexa)
        
        if i == "5":
            make_line_a(alexa)
            alexa.right(90)
            forward_2_then_45_(alexa)
            make_line_c(alexa)
            make_line_d(alexa)
            alexa.right(90)
            forward_2_then_45_(alexa)
            make_line_f(alexa)
            make_line_g(alexa)
            move_turle_zero_position(alexa)
            space_between_numbers(alexa)

        if i == "6":
            # forward_2_then_45_(alexa)
            forward_2_then_45_(alexa)
            alexa.right(90)
            forward_2_then_45_(alexa)
            make_line_c(alexa)
            make_line_d(alexa)
            make_line_e(alexa)
            make_line_f(alexa)
            make_line_g(alexa)
            move_turle_zero_position(alexa)
            space_between_numbers(alexa)

        if i == "7":
            make_line_a(alexa)
            make_line_b(alexa)
            make_line_c(alexa)
            alexa.right(90)
            forward_2_then_45_(alexa)
            alexa.right(90)
            forward_2_then_45_(alexa)
            forward_2_then_45_(alexa)
            alexa.right(90)            
            space_between_numbers(alexa)

        if i == "8":
            make_line_a(alexa)
            make_line_b(alexa)
            make_line_c(alexa)
            make_line_d(alexa)
            make_line_e(alexa)
            make_line_f(alexa)
            make_line_g(alexa)
            move_turle_zero_position(alexa)
            space_between_numbers(alexa)

        if i == "9":
            make_line_a(alexa)
            make_line_b(alexa)
            make_line_c(alexa)
            alexa.right(90)
            forward_2_then_45_(alexa)
            alexa.right(90)
            forward_2_then_45_(alexa)
            make_line_f(alexa)
            make_line_g(alexa)
            move_turle_zero_position(alexa)
            space_between_numbers(alexa)

# Question 13 - 2
def make_line_a(alexa):
    """Draw a particular line/segment, "a", that will serve as a building block for the turtle_draw_numbers()."""
 
    alexa.penup()
    alexa.forward(2)
    alexa.pendown()
    alexa.forward(45)
    alexa.penup()
    alexa.forward(2)
    
# Question 13 - 3
def make_line_b(alexa):
    """Draw a particular line/segment, "b", that will serve as a building block for the turtle_draw_numbers()."""
  
    alexa.right(90)
    alexa.penup()
    alexa.forward(2)
    alexa.pendown()
    alexa.forward(45)
    alexa.penup()

# Question 13 - 4
def make_line_c(alexa):
    """Draw a particular line/segment, "c", that will serve as a building block for the turtle_draw_numbers()."""
    
    alexa.up()
    alexa.forward(2)
    alexa.pendown()
    alexa.forward(45)
    alexa.penup()
    alexa.forward(2)


# Question 13 - 6
def make_line_d(alexa):
    """Draw a particular line/segment, "d", that will serve as a building block for the turtle_draw_numbers()."""
    
    alexa.right(90)
    alexa.pendown()
    alexa.forward(2)
    alexa.pendown()
    alexa.forward(45)
    alexa.penup()
    alexa.forward(2)

# Question 13 - 7
def make_line_e(alexa):
    """Draw a particular line/segment, "e", that will serve as a building block for the turtle_draw_numbers()."""
    
    alexa.right(90)
    alexa.pendown()
    alexa.forward(2)
    alexa.pendown()
    alexa.forward(45)
    alexa.penup()
    alexa.forward(2)

# Question 13 - 8
def make_line_f(alexa):
    """Draw a particular line/segment, "f", that will serve as a building block for the turtle_draw_numbers()."""
    
    alexa.up()
    alexa.pendown()
    alexa.forward(45)
    alexa.penup()
    alexa.forward(2)

# Question 13 - 9
def make_line_g(alexa):
    """Draw a particular line/segment, "g", that will serve as a building block for the turtle_draw_numbers()."""
    
    alexa.right(180)
    alexa.forward(45)
    alexa.left(90)
    alexa.forward(3)
    alexa.pendown()
    alexa.forward(42)
    alexa.penup()
    alexa.forward(2)

# Question 13 - 10
def space_between_numbers(alexa):
    """Create a spacing funtion that allows for space between numbers drawn by the Turle."""

    alexa.penup()
    alexa.setheading(0)
    alexa.forward(60)

# Question 13 - 11
def move_turle_zero_position(alexa):
    """Move Python turtle to the zero start position of each number that has just been 
    drawn for set up for next number(the top left cormer of each number)."""

    alexa.penup()
    alexa.right(180)
    alexa.forward(45)
    alexa.forward(2)
    alexa.right(90)
    alexa.forward(45)

# Question 13 - 12
def forward_2_then_45_(alexa):
    """Move Turtle forward with no lines drawn to position for next drawn move."""
    
    alexa.penup()
    alexa.forward(2)
    alexa.forward(45)


def delay_turtle():
    """Delay start of Python Turtle module. This gives the user time to read instructions & 
    usefull info to user on what to expect from the behavior of the program."""

    import time
    for i in range(1):
        print("*** Note - Python Turtle will commence in 5 seconds.***")
        print("To exit the Python Turtle screen, click on the Turle sand-box when drawing is complete.")
        print("This will allow the rest of the code in this module to execute...\nHappy code viewing!")

        time.sleep(5)

# Shared function for question 12 & 13
def tidy_user_input(user_str):
    """Tidy up user string input, check if string can be converted to integers."""

    numbers_to_draw = user_str.strip(" ")
    numbers_to_draw = numbers_to_draw.replace(" ", "")

    if numbers_to_draw.isdigit():
        return numbers_to_draw
    else:
        user_input = input("Hmmmmm, that's not a number. Please try again: ")
        return tidy_user_input(user_input)


def main():

    #Question 12
    print("Play the roll your own dice game.")
    number_of_sides = input("Please enter in the number of faces on your dice, it must have at lest four sides: ")
    print(toss_dice(number_of_sides))
    print("\n")

    delay_turtle()

    # # Question 13
    import turtle
    screen = turtle.Screen()
    alexa = turtle.Turtle()
    alexa.shape("turtle")
    alexa.speed(4)
    alexa.penup()
    alexa.pendown()

    print("\n")
    print("Python Turtle wants to draw out your number like a seven-segment-indicator!")
    # Question 13 - 2
    user_str = input("Please give the Python Turtle a number you want her to draw, eg. 415, or 2, or even 0169: ")
    cleaned_input = tidy_user_input(user_str)


    turtle_draw_numbers(alexa, cleaned_input)

    
    screen.exitonclick()



main()
