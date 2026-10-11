from asyncio import all_tasks
from turtle import Turtle
Up = 90
Down = 270
Left = 180
Right = 0

class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    # Create a snake's body
    def create_snake(self):
        x = 0

        for i in range(3):
            tim = Turtle(shape="square")
            tim.color("White")
            tim.penup()
            tim.teleport(x, 0)
            x -= 20
            self.all_turtles.append(tim)

    def add_turtle(self):
        tim = Turtle(shape ="square")
        tim.color("white")
        tim.teleport(self.all_turtles[-1].xcor(),self.all_turtles[-1].ycor())
        tim.penup()
        self.all_turtles.append(tim)

    def reset(self):
        for turtle in self.all_turtles:
            turtle.teleport(400,400)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]


    # Animating The snake segments
    def move(self):

        for i in range(len(self.all_turtles) - 1, 0, -1):
            x = self.all_turtles[i - 1].xcor()
            y = self.all_turtles[i - 1].ycor()
            self.all_turtles[i].teleport(x, y)
        self.all_turtles[0].forward(20)
    # Controlling a snake's movements
    def up(self):
        if self.head.heading() != Down:
            self.all_turtles[0].setheading(Up)
    def down(self):
        if self.head.heading() != Up:
            self.all_turtles[0].setheading(Down)
    def left(self):
        if self.head.heading() != Right:
            self.all_turtles[0].setheading(Left)
    def right(self):
        if self.head.heading() != Left:
            self.all_turtles[0].setheading(Right)
