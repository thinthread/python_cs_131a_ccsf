''' 
In Python, a function is a named sequence of statements that belong together. 
Their primary purpose is to help us organize programs into chunks that match how 
we think about the solution to the problem.

Makes code easy to re-use.

keyword def
function_name is what ever you want, same rules as variable names
(pass in paramiters here) - caleld paramiters as a placeholder when first writing the function
and called arguments when passed an object of value. 

function:
def function_name( formal parameters ):
    statement

function call function invocatioin:
functioin_name( passs in arguments here)

(Not all functions have formal parameters/arguemnts(aka - actual parameters))
def print_hello():
    print("Hi there!")

function call or function invocatioin:
print_hello()


'''

####################################################################
# * Note -  You can call a funtion inside of another function - like in recursion(calls it self inside of it self)


def countup(n):
    if n >= 0:
        countup(n - 1)
        print(n)

countup(1)

###

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
    # call a function in a function
    draw_multi_color_square(alexa, length)
    length = length + 10
    alexa.forward(10)
    alexa.right(18)



wn.exitonclick()

###################################################






''' docstrings - <function_name>.__doc__

If the first thing after the function header is a string (some tools insist that it must be a triple-quoted string),
it is called a docstring and gets special treatment in Python and in some of the programming tools.

Another way to retrieve this information is to use the interactive interpreter, and enter the expression <function_name>.__doc__,
which will retrieve the docstring for the function. So the string you write as documentation at the start of a function is retrievable by python tools at runtime. This is different from comments in your code, which are completely eliminated when the program is parsed.

By convention, Python programmers use docstrings for the key documentation of their functions.

'''