def x_cor(velocity, theta, time):
          """Calculate x"""
          import math 
          return ( velocity * math.cos(math.radians(theta))* time)
          

def y_cor(velocity, theta, time, acceleration):
          """Calculate """
          import math 
          return ( velocity * math.sin(math.radians(theta))* time + acceleration * time **2/2)
         
          
def main():
    import turtle

    wn = turtle.Screen()
    alexa = turtle.Turtle()
  
    for time in range(20):
          alexa.goto(x_cor(20,45,time), y_cor(20, 45, time, -10))

    wn.exitonclick()
          
main()