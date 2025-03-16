#create separate functions for square and triangle
import turtle

def draw_square():
    for i in range(0, 4):
        turtle.fd(50)
        turtle.lt(90)
    turtle.fd(75)

def draw_triangle():
    for i in range(0, 3):
        turtle.fd(50)
        turtle.lt(120)
    turtle.fd(75)
turtle.goto(-250,0)

draw_square()
draw_triangle()
draw_square()
draw_triangle()

delay = input("Press enter to finish.")