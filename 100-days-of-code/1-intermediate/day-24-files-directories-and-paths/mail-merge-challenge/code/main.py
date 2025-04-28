with open('../users/invited_users', 'r') as users:
  for user in users:
    with open('../starting_letter/sample', 'r') as file:
      new_letter = file.read()
    new_letter = new_letter.replace("[name]",f"{user.strip()}")
    with open(f"../ready_to_send/{user.strip()}-letter", 'w') as file:
      file.write(new_letter)
