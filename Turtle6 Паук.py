import turtle as tt

x = int(input("Количество лучей: "))
tt.shape('turtle')
for i in range(x):
    tt.forward(100)
    tt.right(180)
    tt.forward(100)
    tt.right(180 + 360 / x)

tt.done()











