import turtle


def proper_polygone (N: int, L: int):
    for step in range (N):
        turtle.forward(L)
        turtle.left(360/N)


x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
proper_polygone (x, y)
