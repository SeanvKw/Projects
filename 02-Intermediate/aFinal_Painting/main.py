import turtle as t
import random
tutel = t.Turtle()
t.colormode(255)


def generate_random_color():
    color_list = [(202, 164, 110), (149, 75, 50), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
                  (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
    return random.choice(color_list)


tutel.hideturtle()
tutel.shape("triangle")
tutel.speed("fastest")
tutel.up()
# Loop through each row (10 rows)
for row in range(10):
    # Loop through each column in the current row (10 columns)
    for col in range(10):
        tutel.dot(20, generate_random_color())  # Draw a dot with random color
        tutel.forward(50)  # Move forward to the next dot position
    # After finishing a row, move up to the next row
    tutel.setheading(-270)  # Point upwards
    tutel.forward(50)       # Move up to the next row
    tutel.setheading(-180)  # Point to the left
    tutel.forward(500)      # Move back to the start of the row
    tutel.setheading(0)     # Point right again for the next row

screen = t.Screen()
screen.exitonclick()
