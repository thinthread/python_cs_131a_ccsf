""" Write a Python function to draw the curve give by y = 100*(cos(x/10)
+cos(x/12) )for a given x range in radians. You do not need to draw axis here.
"""


def cosine_wave(n): # please use n = 200 in a range -n to n
    """ Draw the given cosine curve with Python turtles"""
    import turtle
    import math

    tur = turtle.Turtle()
    
    tur.up()
    ystart = 200*(math.cos(-n/10) + math.cos(-n/12))
    tur.goto(-n, ystart) 
    tur.down()

    for x in range(-n, n):
        y = 200*(math.cos(x/10) + math.cos(x/12))tur.goto(x, y)


    screen.exitonclick()


def main():
    cosine_wave()

main()
