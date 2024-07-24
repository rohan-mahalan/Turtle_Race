from turtle import Turtle


class FINISH(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(310, -200)
        self.setheading(90)
        self.color("red")
        self.pendown()
        self.forward(400)
