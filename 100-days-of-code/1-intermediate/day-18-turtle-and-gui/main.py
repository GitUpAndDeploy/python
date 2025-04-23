import turtle as t
from colors import colors
import random

tim = t.Turtle()
screen = t.Screen()

tim.hideturtle()
tim.color("red")
tim.penup()
tim.goto(-250, -250)
tim.speed("fastest")
grid_size = 10

for i in range(grid_size):
  for _ in range(grid_size):
    tim.dot(20, random.choice(colors))
    if _ < grid_size - 1:
      tim.forward(50)
  if i%2 == 0:
    tim.left(90)
    tim.forward(50)
    tim.left(90)
  else:
    tim.right(90)
    tim.forward(50)
    tim.right(90)


screen.exitonclick()
