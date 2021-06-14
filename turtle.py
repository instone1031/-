import turtle
import random

t = turtle.Turtle()
t.shape("turtle")
t.pencolor("black")


def draw_square(x, y, c):
    t.color(c)
    t.pencolor("black")
    t.penup()
    t.goto(random.randint(-100, 100), random.randint(-100, 100))
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.fd(x)
        t.lt(90)
        t.fd(y)
        t.lt(90)
    t.end_fill()


for i in ['yellow', 'red', 'purple', 'blue']:
    draw_square(100, 100, i)

turtle.mainloop()
turtle.bye()
