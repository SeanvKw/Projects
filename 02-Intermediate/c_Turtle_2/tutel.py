from turtle import Turtle, Screen
import random


def starting_line():
    names = (adrian, molendowski, skrzypczyk, daniel, hubi)
    width = -230
    height = 150
    idx = -1
    for tutel in names:
        idx += 1
        tutel.color(colors[idx])
        tutel.goto(width, height)
        height -= 50


screen = Screen()
screen.setup(500, 800)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a name: ".lower())
colors = ["red", "orange", "yellow", "green", "blue"]

playing = False

adrian = Turtle(shape="turtle")
molendowski = Turtle(shape="turtle")
skrzypczyk = Turtle(shape="turtle")
daniel = Turtle(shape="turtle")
hubi = Turtle(shape="turtle")
names = (adrian, molendowski, skrzypczyk, daniel, hubi)
adrian.up()
molendowski.up()
skrzypczyk.up()
daniel.up()
hubi.up()
starting_line()

if user_bet:
    playing = True

while playing:
    for tutels in names:
        if tutels.xcor() > 230:
            playing = False
            winning_color = tutels.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(
                    f"You've LOST! The {winning_color} turtle is the winner!")
        rand_dist = random.randint(0, 10)
        tutels.forward(rand_dist)
screen.exitonclick()
