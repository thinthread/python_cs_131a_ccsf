""" Turtle draws square. """

import turtle

# Create turtle sandbox (window) and set color
wn = turtle.Screen()
wn.bgcolor("purple")

# Create turtle
alexa = turtle.Turtle()

def draw_square(turtle, size):
    """ Make turtle draw a square with size as a square's side. """

    square = range(4)

    for line in square:
        alexa.forward(size)
        alexa.left(90)

# function call
draw_square(alexa, 50)

wn.exitonclick()

