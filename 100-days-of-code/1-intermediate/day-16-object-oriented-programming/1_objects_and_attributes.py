import turtle
import another_module
from turtle import Turtle, Screen

print(another_module.another_variable)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("pink")

for i in range(360):
  timmy.forward(2)
  timmy.right(1)

for i in range(360):
  timmy.forward(1.75)
  timmy.left(1)

print(timmy)

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()
