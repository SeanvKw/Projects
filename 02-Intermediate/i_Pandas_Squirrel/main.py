import pandas

data = pandas.read_csv(
    "02-Intermediate/j_Pandas_Squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = (sum(data["Primary Fur Color"] == "Gray"))
red = (sum(data["Primary Fur Color"] == "Cinnamon"))
black = (sum(data["Primary Fur Color"] == "Black"))

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray, red, black]
}
df = pandas.DataFrame(data_dict)
df.to_csv("02-Intermediate/j_Pandas_Squirrel/squirrel_count.csv")
