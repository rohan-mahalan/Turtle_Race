from turtle import Turtle
import random
COLORS = ["red", "orange", "blue", "violet", "black"]
POSITION = [(-300, -80), (-300, -30), (-300, 20), (-300, 70), (-300, 120)]
PACES = [10, 15, 20, 25, 30, 35, 40, 45, 50]


class OTHERS:
    def __init__(self):
        self.segments = []
        for i in range(0, 5):
            n = Turtle()
            n.penup()
            n.shape("turtle")
            n.color(COLORS[i])
            n.goto(POSITION[i])
            self.segments.append(n)

    def movement(self):
        for i in self.segments:
            i.forward(random.choice(PACES))
