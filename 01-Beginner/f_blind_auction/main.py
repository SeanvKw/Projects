# TODO-1: Ask the user for input
name = input("What is your name?\n")
price = int(input("What is your bid? \n$"))
# TODO-2: Save data into dictionary {name: price}
bid_details = {name: price}
# TODO-3: Whether if new bids need to be added
auction_start = True
while auction_start:
    new_bid = input("Do you want to add a new bid? (yes/no) ").lower()
    if new_bid == "yes":
        print("\n" * 20)
        name = input("What is your name?\n")
        price = int(input("What is your bid? \n$"))
        bid_details[name] = price
    elif new_bid == "no":
        auction = False
# TODO-4: Compare bids in dictionary
highest_bid = 0
for price in bid_details.values():
    if price > highest_bid:
        highest_bid = price
# TODO-5: Print the winner
print(f"The winner is {name} with a bid of ${highest_bid}.")
