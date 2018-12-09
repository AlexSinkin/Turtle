import turtle
turtle.shape('turtle')
def square (l: int):
    for x in range(4):
        turtle.forward(l)
        turtle.left(90)
    turtle.left(180)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    return

l = 10
for x in range(10):
    square(l)
    l += 20