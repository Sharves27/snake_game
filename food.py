from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color('light blue')
        self.shapesize(0.5,0.5)
        self.speed(0)
        self.penup()
        self.refresh()


    def refresh(self):
        self.goto(x=random.randrange(-260,260,20) , y=random.randrange(-260,260,20))

    