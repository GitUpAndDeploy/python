from prettytable import PrettyTable

# Create a PrettyTable object
table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur", "Jigglypuff"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass", "Fairy"])
table.add_column("Level", [25, 15, 20, 18, 12])
# Add a row to the table
table.add_row(["Eevee", "Normal", 10])
# Add a row to the table
table.add_row(["Mewtwo", "Psychic", 70])
# Add a row to the table
table.add_row(["Gengar", "Ghost", 30])

# table.align = "l"  # Align the columns to the left
table.align["Pokemon"] = "l"  # Align the Pokemon column to the left

# Print the table
print(table)
