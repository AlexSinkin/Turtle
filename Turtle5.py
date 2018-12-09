import turtle as tt

tt.shape('turtle')
x = int(input("Количество лучей: "))
for i in range(x):
    tt.forward(100)
    tt.right(180)
    tt.forward(100)
    tt.right(180 + 360 / x)

tt.done()











