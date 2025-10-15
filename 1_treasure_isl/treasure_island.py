print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossroad = input(str(
    "You're at a crossroad. Where do you want to go? Type 'left' or 'right'.\n")).lower()

if crossroad == "left":
    abandoned_village = input(str(
        "You've come to a abandoned village, There is no treasure around here. You can go 'back or 'right'.\n")).lower()

    if abandoned_village == "right":
        dead_end = input(str(
            "You've come to a dead end. You can only turn around by going 'back'\n")).lower()
        if dead_end == "back":
            print(
                "You've came back to crossroad. Where do you want to go this time? Type 'left' or 'right'.\n")
            crossroad = input().lower()
    if abandoned_village == "back":
        crossroad = input(str(
            "You're at a crossroad. Where do you want to go? Type 'left' or 'right'.\n")).lower()

if crossroad == "right":
    print("You've came to a lake, how do u want to go through it? Type 'swim' or 'boat' \n")
    lake = input().lower()
    if lake == "swim":
        print("Sadly, You didn't make it to the other end of the lake so u LOSE!!!\n")
    elif lake == "boat":
        print("Good job! You are now at the other end and u see a house with 3 doors. Red , Yellow , Blue. Which colour do you choose?\n")
        door = input().lower()
        if door == "red":
            print("It's a room full of fire. Game Over")
        elif door == "yellow":
            print("You found the treasure. You Win!")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell in to a hole. Game Over.")
