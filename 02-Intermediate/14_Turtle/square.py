from turtle import Turtle, Screen

tutel = Turtle()
tutel.shape("turtle")
tutel.color("coral")
for i in range(4):
    tutel.forward(100)  # Move forward by 100 units
    tutel.right(90)      # Turn right by 90 degrees
screen = Screen()
screen.exitonclick()  # Wait for a click to close the window
