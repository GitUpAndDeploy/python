from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
  sleep(ball.move_speed)
  screen.update()
  ball.move()

  # Detect collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    # bounce
    ball.y_bounce()

  # Detect collision with right paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.x_bounce()
  
  # Detct when right paddle misses
  if ball.xcor() > 380:
    scoreboard.l_point()
    ball.reset_position()

  if ball.xcor() < -380:
    scoreboard.r_point()
    ball.reset_position()


screen.exitonclick()
