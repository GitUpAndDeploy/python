import pandas as p

data  = p.read_csv("squirrel_data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == 'Gray'])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrels_count = len(data[data["Primary Fur Color"] == 'Black'])

data_dict = {
  "Primary Fur Color" : ["Gray", "Cinnamon", "Black"],
  "Count" : [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

out_data = p.DataFrame(data_dict)

out_data.to_csv("squirrels.csv")
