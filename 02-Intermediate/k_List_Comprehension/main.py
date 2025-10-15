numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)

new_list = [n*2 for n in range(1, 5)]
print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_list = [short_names for short_names in names if len(short_names) <= 4]
print(new_list)

new_list = [short_names.upper()
            for short_names in names if len(short_names) > 5]
print(new_list)
