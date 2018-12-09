import turtle as tt
from math import *

tt.shape('turtle')
x = int(input("Количество сторон: "))
for i in range(x):
    tt.forward(2 * pi * 100 / x)
    tt.right(360 / x)

tt.done()











