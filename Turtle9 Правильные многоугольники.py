from math import *
import turtle as tt

n = 10
radius = 40
shift = 25

tt.shape("turtle")
tt.penup()
tt.goto(50, 50)
tt.pendown()

for i in range(3, n):
    tt.left((180 - 360 / i) / 2)
    for j in range(i):
        tt.left(360 / i)
        tt.forward(2 * pi * (radius + shift * (i - 3)) / i)
    tt.right((180 - 360 / i) / 2)
    tt.penup()
    tt.forward(shift - 5)
    tt.pendown()

tt.done()
