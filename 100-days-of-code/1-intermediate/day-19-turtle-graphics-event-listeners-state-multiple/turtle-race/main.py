from turtle import Turtle, Screen
import random
from colors import colors

screen = Screen()
screen.setup(width=540, height=450)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = []
for index, value in enumerate(colors):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(-250, 200 - index * 50)
    turtle.pendown()
    turtles.append(turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 250:
          print(f"{turtle.pencolor()} turtle is the winner!")
          if user_bet == turtle.pencolor()[0]:
            print("You win!")
          else:
            print("You lose!")
          is_race_on = False


def move_turtle(turtle):
    distance = random.randint(1, 10)
    turtle.forward(distance)



screen.exitonclick()
