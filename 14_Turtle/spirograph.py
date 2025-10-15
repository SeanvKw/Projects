import turtle as t
import random
tutel = t.Turtle()
tutel.shape("turtle")
t.colormode(255)
tutel.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tutel.color(random_color())
        tutel.circle(100)
        tutel.setheading(tutel.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
