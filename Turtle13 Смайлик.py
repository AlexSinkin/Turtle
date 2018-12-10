import turtle as tt

tt.shape('turtle')

# Голова
tt.color('black', 'yellow')
tt.begin_fill()
tt.circle(100)
tt.end_fill()

# Правый глаз
tt.penup()
tt.goto(50, 120)
tt.pendown()
tt.color('black', 'blue')
tt.begin_fill()
tt.circle(15)
tt.end_fill()

# Левый глаз
tt.penup()
tt.goto(-50, 120)
tt.pendown()
tt.color('black', 'blue')
tt.begin_fill()
tt.circle(15)
tt.end_fill()

# Нос
tt.penup()
tt.goto(0, 115)
tt.right(90)
tt.pendown()
tt.color('black')
tt.width(10)
tt.forward(40)

# Рот
tt.penup()
tt.goto(-50, 50)
tt.pendown()
tt.left(30)
tt.color('red')
tt.circle(60, 120)

tt.done()
