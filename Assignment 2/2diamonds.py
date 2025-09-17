import turtle
import math


side = 120

def draw_diamond():
    turtle.begin_fill()
    turtle.right(45)

    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)
    turtle.left(45)
    turtle.end_fill()


turtle.color("red")

width = 2 * side * math.sqrt(2)

# Draw first diamond
turtle.penup()
turtle.backward(width / 2 - (side * math.sqrt(2)) / 2)
turtle.pendown()
draw_diamond()

# Draw second diamond
turtle.penup()
turtle.forward(side * math.sqrt(2))
turtle.pendown()
draw_diamond()





