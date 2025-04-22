# # Class name must be in Pascal case
# class User:
#   pass

# user_1 = User()

# # Creating attributes
# user_1.id = "001"
# user_1.username = "johndoe"

# print(user_1.id)


# # Constructor
# class User:
#   def __init__(self, user_id, username , followers):
#     self.id = user_id
#     self.username = username
#     self.followers = 0

# user_1 = User("001", "johndoe")
# user_2 = User("002", "janedoe")


class User:
  def __init__(self, user_id, username):
    """Initializes the user with an ID, username, and followers."""
    self.id = user_id
    self.username = username
    self.followers = 0
    self.following = 0

  def follow(self, user):
    """Follows a user."""
    user.followers += 1
    self.following += 1
    print(f"{self.username} followed {user.username}")

user_1 = User("001", "johndoe")
user_2 = User("002", "janedoe")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
