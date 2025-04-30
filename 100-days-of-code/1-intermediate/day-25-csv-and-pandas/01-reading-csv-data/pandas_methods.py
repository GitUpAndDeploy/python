import pandas

data = pandas.read_csv("../weather_data.csv")

# print(data["temp"])

# # Dataframe
# print(type(data))

# # Series, two ways to do it, fet data in columns
# print(type(data["temp"]))
# print(data.temp)

# # Convert to a list
# temp_list = data["temp"].to_list()

# print(temp_list)

# print(data["temp"].mean())

# print(data["temp"].max())

# print(data.temp)

# # Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Get specific column and row
print(data[data.day == "Monday"].condition)

def fahrenheit(temp):
  temp = temp * 1.8 + 32
  return float(temp)

print(fahrenheit(data[data.day == "Monday"].temp))

