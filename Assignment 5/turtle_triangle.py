import turtle

def triangle(points, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[0])
    turtle.end_fill()

def main():
    turtle.speed(1)

    # Points
    A = (0, 0)
    B = (100, 0)
    D = (-100, 0)    
    C = (0, -150)   
    F = (-100, -300)
    G = (100, -300)

   
    triangle([A, D, C], "green")
    triangle([A, B, C], "red")
    triangle([C, G ,F], "blue")

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
