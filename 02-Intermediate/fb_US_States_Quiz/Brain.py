from turtle import Turtle
import pandas


class Brain(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.guessed_states = []
        self.hideturtle()
        self.penup()
        self.data = pandas.read_csv(
            "02-Intermediate/j_US_States_Quiz/50_states.csv")
        self.states_list = self.data["state"].to_list()

    def guess(self, answer_state):
        """Process a guessed state."""
        if answer_state in self.states_list and answer_state not in self.guessed_states:
            self.guessed_states.append(answer_state)
            self.score += 1

            state_data = self.data[self.data.state == answer_state]
            x = int(state_data['x'].values[0])
            y = int(state_data['y'].values[0])

            self.goto(x, y)
            self.write(answer_state, align="center",
                       font=("Arial", 12, "normal"))

    def score_count(self):
        """Check if all states are guessed and end the game."""
        if self.score == 50:
            self.goto(0, 0)
            self.write("CONGRATS YOU WON!!!!", align="center",
                       font=("Arial", 20, "normal"))
            return True
        return False

    def not_guessed(self):
        # for self.state in self.states_list:
        #     if self.state not in self.guessed_states:
        #         self.missing_states.append(self.state)
        self.unguessed_states = [
            self.state for self.state in self.states_list if self.state not in self.guessed_states]
        self.new_data = pandas.DataFrame(self.unguessed_states)
        self.new_data.to_csv(
            "02-Intermediate/j_US_States_Quiz/states_to_learn.csv")
