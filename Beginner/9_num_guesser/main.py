from art import logo
import random
print(logo)
print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100.")


def num_ran():
    return random.randint(1, 100)


def num_of_lives(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        return 0


def guess_the_number(difficulty, user_num):
    number_to_guess = num_ran()
    lives = num_of_lives(difficulty)
    print(
        f"Psst. That's ur number just to check if the code works {number_to_guess}\n")
    game_over = False

    while not game_over:
        if user_num == number_to_guess and lives > 0:
            print("Congrats! You guessed the right number!!!")
            print(f"You had {lives} left.")
            game_over = True

        else:
            if user_num > number_to_guess:
                print("Too high!")
            else:
                print("Too low!")

            lives -= 1
        if lives == 0:
            print("You've run out of lives. Game Over!")
            print(f"The correct answer was {number_to_guess}")
            game_over = True
        else:
            print(f"You have {lives} lives left.")
            user_num = int(input("Try again: "))


guess_the_number(difficulty=input("Choose a difficulty. Type 'easy' or 'hard' ").lower(),
                 user_num=int(input("Guess the number: ")))
