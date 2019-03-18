import turtle
def circle(x,y,radius,color):
    turtle.penup()
    turtle.goto(x,y-radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill

