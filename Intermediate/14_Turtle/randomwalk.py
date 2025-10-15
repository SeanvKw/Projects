import turtle as t
import random
tutel = t.Turtle()
tutel.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


directions = [0, 90, 180, 270]
tutel.pensize(10)

for i in range(1, 200):
    tutel.color(random_color())
    tutel.forward(40)
    tutel.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
