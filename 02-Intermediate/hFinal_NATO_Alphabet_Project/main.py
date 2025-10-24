import pandas

data = pandas.read_csv(
    "02-Intermediate/ha_NATO_Alphabet_Project/nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ").upper()

    try:
        output_list = [nato_alphabet[letter] for letter in user_input]

    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
