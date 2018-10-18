

def draw_polygon(side_length, number_sides, alexa):
    """ draw a polygon"""
    
    angle = 360/number_sides

    for i in range(number_sides):
        turtle.forward(side_length)
        turtle.left(angle)





def main():

    import turtle
    wn = turtle.Screen()
    alexa = turtle.Turtle()

    draw_polygon(40, 3, alexa)


main()