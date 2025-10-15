# Our Blackjack Game House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def blackjack():
    start_of_the_game = input(
        "Do you want to start a new game? Type 'y' or 'n': ").lower()
    if start_of_the_game == "y":
        print("\n" * 20)
        print(art.logo)

        start = True
        computer_cards = []
        user_cards = []  # Randomly select 2 cards from the list

        computer_cards.append(random.sample(cards, k=1))
        print(f"Dealer cards are: {computer_cards[0]}\n")
        user_cards.append(random.sample(cards, k=2))  # User gets two cards
        print(f"Your cards are: {user_cards[0]}")
        print(f"Your sum of cards is: {sum(user_cards[0])}\n")

        while start:
            if sum(user_cards[0]) > 21 and 11 not in user_cards[0]:
                print("You have exceeded 21, you lose!")
                return blackjack()

            elif sum(user_cards[0]) > 21 and 11 in user_cards[0]:
                user_cards[0][user_cards[0].index(11)] = 1
                print(f"Your new cards are with Ace: {user_cards[0]}")
                print(
                    f"Your new sum of cards with Ace as 1: {sum(user_cards[0])}")

            if sum(computer_cards[0]) > 21 and 11 not in computer_cards[0]:
                print("Dealer has exceeded 21, you win!")
                return blackjack()

            elif sum(computer_cards[0]) > 21 and 11 in computer_cards[0]:
                computer_cards[0][computer_cards[0].index(11)] = 1
                print(
                    f"Dealer's new cards are with Ace: {computer_cards[0]}")
                print(
                    f"Dealer's new sum of cards with 1 as Ace: {sum(computer_cards[0])}\n")
            another_card = input(
                "Do you want to draw another card? Type 'y' or 'n': ").lower()

            if another_card == "y":
                user_cards[0].append(random.choice(cards))
                print(f"Your new cards are: {user_cards[0]}")
                print(f"Your new sum of cards is: {sum(user_cards[0])}")
            elif another_card == "n":
                while sum(computer_cards[0]) < 17:
                    computer_cards[0].append(random.choice(cards))
                print(f"Dealer's final cards are: {computer_cards[0]}")
                print(
                    f"Dealer's final sum of cards is: {sum(computer_cards[0])}")

                if sum(computer_cards[0]) > 21 or sum(user_cards[0]) > sum(computer_cards[0]):
                    print("You win!")
                    return blackjack()
                elif sum(user_cards[0]) < sum(computer_cards[0]):
                    print("You lose!")
                    return blackjack()
                else:
                    print("It's a draw!")
                    return blackjack()
    elif start_of_the_game == "n":
        print("Okay, have a nice day!")
        start = False
blackjack()
