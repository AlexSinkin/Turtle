import turtle as tt


def square(l: int):
    for j in range(4):
        tt.forward(l)
        tt.left(90)

    tt.left(180)
    tt.penup()
    tt.forward(10)
    tt.left(90)
    tt.forward(10)
    tt.left(90)
    tt.pendown()
    return


m = 10

tt.shape('turtle')
for i in range(10):
    square(m)
    m += 20
