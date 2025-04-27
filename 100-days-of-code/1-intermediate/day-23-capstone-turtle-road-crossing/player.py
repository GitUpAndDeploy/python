from turtle import Turtle

MOVING_DISTANCE = 10
STARTING_POSITION = (0,-280)

class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.color("black")
    self.penup()
    self.left(90)
    self.goto(STARTING_POSITION)

  def go_up(self):
    self.new_y = self.ycor() + MOVING_DISTANCE
    self.goto(self.xcor(), self.new_y)

  def level_up(self):
    self.goto(STARTING_POSITION)
