from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len = 1,stretch_wid = 1)
        self.color("blue")
        self.speed("fastest")
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.teleport(x, y)
    def move(self):
        x = random.randint(-260,260)
        y = random.randint(-260,260)
        self.teleport(x,y)
