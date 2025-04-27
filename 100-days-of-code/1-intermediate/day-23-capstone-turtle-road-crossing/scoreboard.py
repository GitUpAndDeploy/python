from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("black")
    self.penup()
    self.hideturtle()
    self.level = 1
    self.update_scoreboard()
  
  def update_scoreboard(self):
    self.clear()
    self.goto(-200,260)
    self.write("Level: " + str(self.level), align=ALIGNMENT, font=FONT)
  
  def next_level(self):
    self.level += 1
    self.update_scoreboard()
  
  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

