import turtle

turtle.shape('turtle')


def move_turtle(cmd):
    if cmd == 'F':
        turtle.forward(a)
    elif cmd == 'L':
        turtle.left(60)
    else:
        turtle.right(120)
    return


def kokh_star(moves_in, n):
    if n == 0:
        return moves_in
    else:
        moves_out = []
        for move1 in moves_in:
            if move1 == 'F':
                moves_out.extend(kokh_star(('F', 'L', 'F', 'R', 'F', 'L', 'F'), n - 1))
            else:

                moves_out.append(move1)
    return moves_out


# начальные значения

m = 2
a = int(500 / (3 ** m))

turtle.Screen().setup(1000, 800, 0, 0)

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()

# Launch turtle
for move in kokh_star(('F', 'R', 'F', 'R', 'F'), m):
    move_turtle(move)

turtle.Screen().exitonclick()
