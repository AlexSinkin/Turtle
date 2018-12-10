import turtle as tt

tt.shape('turtle')

tt.right(90)
for i in range(10):
    radius = 50 + 10 * (i - 1)
    tt.circle(radius)
    tt.circle(-radius)
