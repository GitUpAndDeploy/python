class Animal:
  def __init__(self):
    self.num_eyes = 2
  
  def breathe(self):
    print(f"Inhale, exhale.")

# Fish inherits from Animal
# The Fish class is a subclass of the Animal class
class Fish(Animal):
  def __init__(self):
    super().__init__()

  # Update the breathe method to include a message specific to fish
  def breathe(self):
    super().breathe()
    print("Doing this underwater.")

  def swim(self):
    print("Moving in water.")


nemo = Fish()
# Call the methods from the Fish class
nemo.swim()
# Call the methods from the Animal class
nemo.breathe()
print(nemo.num_eyes)
