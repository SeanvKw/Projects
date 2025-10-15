from turtle import Turtle, Screen

tutel = Turtle()
tutel.shape("turtle")
tutel.color("coral")
for i in range(15):
    if i % 2 == 1:
        tutel.forward(10)
        tutel.up()
    else:
        tutel.down()
        tutel.forward(10)
        tutel.up()


screen = Screen()
screen.exitonclick()  # Wait for a click to close the window
