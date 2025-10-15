# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"
inv = []
for line in open("projekty/21_inputs/Input/Names/invited_names.txt").readlines():
    names = line.strip("\n")
    inv.append(names)

for each_name in inv:
    listy = open("projekty/21_inputs/Input/Letters/starting_letter.txt")
    listy_contents = listy.read()
    new_letter = listy_contents.replace(PLACEHOLDER, each_name)
    with open(f"projekty/21_inputs/Output/ReadyToSend/letter_for_{each_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)

        # Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
        # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
