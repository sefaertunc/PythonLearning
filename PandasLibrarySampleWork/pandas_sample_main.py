import pandas as pd


squirrel_data = pd.read_csv("NYC_Squirrels.csv")
primary_fur_color = squirrel_data["Primary Fur Color"]

cinnamon_count = len(squirrel_data[primary_fur_color == "Cinnamon"])
gray_count = len(squirrel_data[primary_fur_color == "Gray"])
black_count = len(squirrel_data[primary_fur_color == "Black"])

squirrel_counts = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "Count": [cinnamon_count, gray_count, black_count]
}

pd.DataFrame(squirrel_counts).to_csv("squirrel_counts.csv")
