def draw_pie_slice(alex, radius, angle, color):
    """Turtle draws pie slice."""
    alex.color("black", color)
    alex.begin_fill()
    alex.circle(radius, angle)   # draw arc
    alex.left(90) #turn towards center
    alex.forward(radius) # draw towards center
    alex.left(180 - angle) #turn back
    alex.forward(radius)
    alex.up()
    alex.left(90)
    alex.end_fill()
    alex.circle(radius, angle) # move turtle to the new location
    alex.pendown()
    
def draw_pie_chart(alex, radius, angle1, angle2, angle3):
    """Turtle draws three part pie chart"""
    draw_pie_slice(alex, radius, angle1, "red")
    draw_pie_slice(alex, radius, angle2, "green")
    draw_pie_slice(alex, radius, angle3, "blue")
    
def main():
    import turtle          
    wn = turtle.Screen()       
    alex = turtle.Turtle()     
    draw_pie_chart(alex, 100, 60, 120, 180)

    
main()
    