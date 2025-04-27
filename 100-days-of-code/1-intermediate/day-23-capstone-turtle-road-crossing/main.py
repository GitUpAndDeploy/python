from turtle import Screen
from time import sleep
from player import Player
from scoreboard import Scoreboard
from cars import Cars


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road crossing")
screen.tracer(0)
move_speed = 0.1

player = Player()
scoreboard = Scoreboard()
cars = Cars()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
  sleep(move_speed)
  screen.update()
  cars.new_car()
  cars.move_cars()
  if player.ycor() > 280:
    player.level_up()
    scoreboard.next_level()
    cars.level_up()
    
  # Detect collision with cars
  for car in cars.all_cars:
    if car.distance(player) < 20:
      game_is_on = False
      scoreboard.game_over()

screen.exitonclick()
