from turtle import Turtle
from colors import colors
import random

STARTING_MOVE_DISTANCE = 5
SPEED_INCREMENT = 10

class Cars(Turtle):
  def __init__(self):
    self.all_cars = []
    self.car_speed = STARTING_MOVE_DISTANCE
  
  def new_car(self):
    random_probability = random.randint(1,6)
    if random_probability == 1:
      new_car = Turtle("square")
      new_car.shapesize(stretch_wid=1, stretch_len=2)
      new_car.penup()
      new_car.color(random.choice(colors))
      random_y = random.randint(-250, 250)
      new_car.goto(300, random_y)
      self.all_cars.append(new_car)

  def move_cars(self):
    for car in self.all_cars:
      car.backward(self.car_speed)

  def level_up(self):
    self.car_speed += SPEED_INCREMENT