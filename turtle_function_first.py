#Add color to the draw_shape function
#Let's think algorithmically
#Add constants
import turtle

#Define constants
#Use capital letters
SQUARE = 4
TRIANGLE = 3
PENTAGON = 5
HEXAGON = 6

def draw_shape(sides, color):
    
    turtle.color(color)

    for i in range(0,sides):
        turtle.fd(50)
        turtle.lt(360/sides)
    turtle.fd(75)

draw_shape(SQUARE, "blue")
draw_shape(TRIANGLE, "red")
draw_shape(PENTAGON, "green")
draw_shape(HEXAGON, "purple")

delay = input("Press enter to finish.")