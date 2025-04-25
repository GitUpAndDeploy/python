from turtle import Screen, Turtle
from snake import Snake
from time import sleep


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off the screen updates

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)  # Sleep for 0.1 seconds to control the speed of the animation
    snake.move()


screen.exitonclick()
