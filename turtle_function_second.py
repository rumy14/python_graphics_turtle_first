#create separate functions for square and triangle
import turtle

def draw_shape(shape, color):

    turtle.color(color)

    if shape == "square":
        for i in range(0, 4):
            turtle.fd(50)
            turtle.lt(90)
        turtle.fd(75)
    if shape == "triangle":
        for i in range(0, 3):
            turtle.fd(50)
            turtle.lt(120)
        turtle.fd(75)
turtle.goto(-250,0)

draw_shape("square", "blue")
draw_shape("triangle", "red")
draw_shape("square", "green")
draw_shape("triangle", "purple")

delay = input("Press enter to finish.")