from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.change_position()

    def change_position(self):
        xcor = random.randrange(-340, 340, 20)
        ycor = random.randrange(-280, 280, 20)
        self.setpos(xcor, ycor)
