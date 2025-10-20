from turtle import Turtle, Screen

ekran = Screen()
tim = Turtle()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()


def penup():
    tim.up()


def pendown():
    tim.down()


ekran.listen()
ekran.onkey(key="w", fun=move_forwards)
ekran.onkey(key="s", fun=move_backwards)
ekran.onkey(key="a", fun=move_left)
ekran.onkey(key="d", fun=move_right)
ekran.onkey(key="c", fun=clear)
ekran.onkey(key="e",  fun=penup)
ekran.onkey(key="f",  fun=pendown)
ekran.exitonclick()
