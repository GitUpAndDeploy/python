import pandas as p

data_dict = {
  "students": ["Amy", "James", "Angela"],
  "scores": [76, 56, 65]
}

data = p.DataFrame(data_dict)

print(data)

data.to_csv("new_data.csv")