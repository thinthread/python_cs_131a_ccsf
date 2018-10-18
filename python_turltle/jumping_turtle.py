import math
import random

def x_coordinate(velocity, theta, time):
    """ return x coordinate"""
    return (velocity*math.cos(math.radians(theta)) * time)

def y_coordinate(velocity, theta, time, acceleration):
    """Return y coordinate"""
    return (velocity*math.sin(math.radians(theta)) * time + acceleration * time ** 2/2)


def jumping_turtle(velocity, theta, time):
    import turtle

    alex = turtle.Turtle()
    sc = turtle.Screen()
    sc.bgcolor("lightgreen")

alex.speed(10)
for i in range(time):
    alex.goto(x_coordinate(velocity, random.randint(0,360), i), y_coordinate(velocity, theta, i, -10))

def fire_works(velocity, time, number):
    import random
for i in range(number):
    jumping_turtle(velocity, random.randint(0, 360), time)


def main():


    fire_works(60, 20, 6)

    sc.exitonclick()
main()