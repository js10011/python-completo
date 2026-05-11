import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)


def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

order = 3  # Você pode mudar a ordem para ver diferentes níveis do fractal
size = 300  # Ajuste o tamanho conforme necessário

koch_snowflake(t, order, size)

t.hideturtle()
screen.mainloop()