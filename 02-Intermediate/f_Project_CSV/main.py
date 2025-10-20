# import csv
# with open("02-Intermediate/i_Project_CSV/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
import pandas

data = pandas.read_csv("02-Intermediate/h_Project_CSV/weather_data.csv")

# data_dict = data.to_dict()

print(data.temp)
# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in Columns
# print(data["condition"])
# print(data.condition)
# print(data.temp)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp
monday_temp_to_farenh = monday_temp * 1.8 + 32
print(monday_temp_to_farenh)

# Create a dataframe from scratch
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("02-Intermediate/h_Project_CSV/pogoda.csv")
