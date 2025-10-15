import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#  0,1 0,2 1,0  1,2 2,0 2,1
list_of_hands = [rock, paper, scissors]
choose_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choose_hand >= 0 and choose_hand <= 2:

    print(list_of_hands[int(choose_hand)])
    random_hand = random.choice(list_of_hands)
    print(f"Computer chose: \n{random_hand}")

    if random_hand == list_of_hands[int(choose_hand)]:
        print("It's a tie!")
    elif random_hand == rock and list_of_hands[int(choose_hand)] == paper:
        print("You won!")
    elif random_hand == rock and list_of_hands[int(choose_hand)] == scissors:
        print("You lose!")
    elif random_hand == paper and list_of_hands[int(choose_hand)] == rock:
        print("You lose!")
    elif random_hand == paper and list_of_hands[int(choose_hand)] == scissors:
        print("You won!")
    elif random_hand == scissors and list_of_hands[int(choose_hand)] == rock:
        print("You won!")
    elif random_hand == scissors and list_of_hands[int(choose_hand)] == paper:
        print("You lose!")
else:
    print("You typed an invalid number, you lose!")
