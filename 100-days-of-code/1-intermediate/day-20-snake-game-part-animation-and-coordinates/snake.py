from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtle_segments = []
        self.create_snake()
        self.head = self.turtle_segments[0]
        self.speed = 20

    def create_snake(self):
        for position in STARTING_POSITIONS:
          new_segment = Turtle("square")
          new_segment.color("white")
          new_segment.penup()
          new_segment.goto(position)
          self.turtle_segments.append(new_segment)
    
    def move(self):
        for seg_num in range(len(self.turtle_segments) - 1, 0, -1):
            new_x = self.turtle_segments[seg_num - 1].xcor()
            new_y = self.turtle_segments[seg_num - 1].ycor()
            self.turtle_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)