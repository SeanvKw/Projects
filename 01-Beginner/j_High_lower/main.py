from game_data import data
import art
import random


def format_data(account):
    """Format the account data into printable format."""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Check if the user's guess is correct."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


print(art.logo)  # type: ignore
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    # move correct answer to the next round as first option
    account_a = account_b
    # generate new account_b so the old one will become account_a if user guessed right
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(
        f"Compare A: {format_data(account_a)}.")

    print(art.vs)  # type: ignore

    print(
        f"Against B: {format_data(account_b)}.")

    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # clear the screen after guess right or wrong.
    print("\n" * 20)
    print(art.logo)  # type: ignore
    # get follower count of each account
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    # check if guess is correct
    is_correct = check_answer(guess, a_followers, b_followers)

    # track score + 1 for each correct answer and lose if incorrect
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

    # repeat game until user loses
