states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
print(states_of_america[1])
print(states_of_america[-1])

states_of_america.pop() # removes the last item
print(states_of_america)

states_of_america.sort() # sorts the list in alphabetical order
print(states_of_america)

states_of_america.reverse() # reverses the list
print(states_of_america)

states_of_america[1] = "Pencilvania"
print(states_of_america[1])

states_of_america.append("New Mexico") # adds to the end of the list
print(states_of_america)

states_of_america.extend(["New Mexico", "Arizona"]) # adds multiple items at the end of the list
print(states_of_america)

states_of_america.insert(0, "New Hampshire") # Adds to the specified index
print(states_of_america)

states_of_america.remove("New Hampshire") # removes the specified item
print(states_of_america)

print(states_of_america[0:3])
print(states_of_america[-3:])
print(states_of_america[0:3])
print(states_of_america[3:6])
print(states_of_america[3:6])
print(states_of_america[3:])
print(states_of_america[:3])
print(states_of_america[::2])
print(states_of_america[1::2])
print(states_of_america[::-1])
print(states_of_america[-1])
print(states_of_america[-3:-1])