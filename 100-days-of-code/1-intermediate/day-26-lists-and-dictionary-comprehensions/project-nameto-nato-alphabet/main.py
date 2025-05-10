import pandas as pd

nato_df = pd.read_csv("nato_alphabet.csv")

nato_dict = {row.letter:row.code for (index,row) in nato_df.iterrows()}

name = input("Please enter your name: ").upper()

nato_name = [nato_dict[letter] for letter in name]

print(nato_name)
