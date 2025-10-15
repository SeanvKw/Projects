from turtle import Screen
from Brain import Brain

# Setup screen
screen = Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491)
screen.bgpic("02-Intermediate/j_US_States_Quiz/blank_states_img.gif")

# Create brain instance
brain = Brain()

# Game loop
game_end = False
while not game_end:
    answer_state = screen.textinput(
        title=f"{brain.score}/50 States Correct", prompt="What's another state's name?".title())

    if not answer_state:  # Cancel or empty input
        game_end = True
        brain.not_guessed()
        print(brain.unguessed_states)
        break

    answer_state = answer_state.title()  # Normalize capitalization
    brain.guess(answer_state)

    if brain.score_count():  # All states guessed
        game_end = True

screen.exitonclick()
