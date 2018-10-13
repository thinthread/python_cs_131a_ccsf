# Questoin 12
def print_phrase(phrase):
    """Print the word Pyhton from the given phrase."""
    print(phrase[:6])

# Question 13    
def print_power_2():
    """Print out the powers of 2, up to"""
    for i in range(0,511):
        i += 2
        print(i, end= " ")

# AND a second answer to Quesiton 13
def geo_series(a,r,limit):
    """Print geo series, with start as a, step by r and limit is end."""   
    
    term = 2
    while term <= limit:
        print(term, end = " ")
        term += r

# Question 14    
def draw_curve(n):
    """"Use Python Turtle to draw a physics modulation curve"""
    import turtle
    import math
    screen = turtle.Screen()
    alexa =  turtle.Turtle()
    
    alexa.penup()
    alexa.goto(-n, 0)
    alexa.pendown()
    
    for x in range(-n, n):
        y = 100*(math.cos(x/10)+math.cos(1*x/12))
        alexa.goto(x,y)

        
    screen.exitonclick()
 
# Question 15   
def lognm(n,m):
    """Return the logarithmic value of any given number with respect to any given base."""
    import math
    return math.log10(n)/math.log10(m)

# Question 16
def spell_python_correctly(str, n):
    """Slice the back end of a tring and add it to the front of a string, use string rotation"""
    return str[n:] + str[0:n]    

    
def main():
    """Call all functions """
    # Question 12
    print_phrase("Python Programming")
    
    # Question 13
    print_power_2()
    
    # AND a second answer to Quesiton 13
    geo_series(2, 2, 512)
    
    # Question 14
    draw_curve(200)

    # Question 15
    print(lognm(1000,10))

    # Question 16
    print(spell_python_correctly("Python", 2))
    
main()
