class Car:
  def __init__(self, **kw):
    self.make = kw["make"]
    self.model = kw["model"]

my_car = Car(make = "Polestar", model = "Polestar 2")

print(my_car.make)
print(my_car.model)
