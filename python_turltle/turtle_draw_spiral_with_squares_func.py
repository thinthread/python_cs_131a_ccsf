''' Draws a multicolor spiral using layers of off set squares that increase in size as they layer.'''

import turtle


wn = turtle.Screen()
wn.bgcolor("lightgreen")

alexa = turtle.Turtle()
turtle.pensize(3)


def draw_multi_color_square( turtle, length):
    """ Make a turtle draw square. Each line(length) of the square is a different color"""

    for line in ['red', 'purple', 'hotpink', 'blue']:
        alexa.color(line)
        alexa.forward(length)
        alexa.left(90)

length = 20
for square in range(15):
    draw_multi_color_square(alexa, length)
    length = length + 10
    alexa.forward(10)
    alexa.right(18)



wn.exitonclick()


