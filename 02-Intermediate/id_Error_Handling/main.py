# FileNotFoundEror
# try:
#     with open("a_file.txt") as file:
#         file.read()
# except FileNotFoundError:
#     print("This directory does not exist!!")

# KeyError
# try:
#     a_dict = {"key": "value"}
#     value = a_dict['non_existent_key']
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist!")

# IndexError
# try:
#     fruit_list = ["Apple", "Banana", "Pear"]
#     fruit = fruit_list[3]
# except IndexError as error_message:
#     print(f"{error_message}")
# TypeError
# try:
#     text = "abc"
#     print(text + 5)  # type: ignore
# except TypeError as type_error:
#     print(f"{type_error} Don't do that man :D")
# finally:
#     raise KeyError("This is an error that I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 300:
    raise ValueEror("You are not that tall!")
bmi = weight / height ** 2
primt(bmi)
