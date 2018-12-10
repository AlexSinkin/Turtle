import turtle as tt
from math import *

x = int(input("Количество сторон: "))
tt.shape('turtle')
for i in range(x):
    tt.forward(2 * pi * 100 / x)
    tt.right(360 / x)

tt.done()











