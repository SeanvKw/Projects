import turtle as t
import random
tutel = t.Turtle()
tutel.shape("turtle")


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tutel.speed("fastest")


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tutel.forward(100)
        tutel.right(angle)


for shape_side_n in range(3, 36):
    tutel.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = t.Screen()
screen.exitonclick()
