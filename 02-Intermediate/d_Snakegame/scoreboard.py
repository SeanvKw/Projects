from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("White")
        self.up()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.read_files()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,
                   font=FONT)
        self.data.close()

    def reset(self):
        if self.score > self.high_score:
            self.f = open("01-Beginner/d_Snakegame/data.txt", mode="w")
            self.f.write(repr(self.score))
            self.f.close()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_files(self):
        self.data = open("01-Beginner/d_Snakegame/data.txt", mode="r")
        self.high_score = int(self.data.read())

    def write_to_files(self):
        self.f = open("01-Beginner/d_Snakegame/data.txt", mode="w")
        self.f.write(repr(self.score))
        self.f.close()
