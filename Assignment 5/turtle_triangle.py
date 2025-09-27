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
    turtle.speed(3)  
    
    # Triangle 1
    triangle([(0, 0), (100, 0), (50, 100)], "red")
    
    # Triangle 2
    triangle([(-150, -50), (-50, -50), (-100, 50)], "blue")
    
    # Triangle 3
    triangle([(150, -50), (250, -50), (200, 50)], "green")

    turtle.done()

if __name__ == "__main__":
    main()

    