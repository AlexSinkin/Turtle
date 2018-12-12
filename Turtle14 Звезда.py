import turtle as tt


def draw_star(turtle, n):
    for i in range(n):
        turtle.forward(200)
        turtle.left(180 - (360 / (2 * n)))
    return


def draw_star5():
    global turtle1_n
    turtle1.forward(200)
    turtle1.left(180 - (360 / (2 * 5)))
    turtle1_n += 1
    if turtle1_n < 5:
        screen.ontimer(draw_star5, 900)
    return


def draw_star11():
    global turtle2_n
    turtle2.forward(200)
    turtle2.left(180 - (360 / (2 * 11)))
    turtle2_n += 1
    if turtle2_n < 11:
        screen.ontimer(draw_star11, 300)
    return


def create_turtle(x, y):
    turtle = tt.Turtle()
    turtle.shape('turtle')
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    return turtle


screen = tt.Screen()

turtle1 = create_turtle(-50, 0)
turtle1.left(180)
turtle1_n = 0
screen.ontimer(draw_star5, 1000)
# draw_star(turtle1, 5)

turtle2 = create_turtle(200, 0)
turtle2.left(180)
turtle2_n = 0
screen.ontimer(draw_star11, 1100)
# draw_star(turtle2, 11)

screen.mainloop()

