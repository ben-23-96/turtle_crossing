from turtle import Turtle


class Player_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')

    def start(self):
        self.setposition((0, -300))
        self.setheading(90)

    def move(self):
        self.forward(20)

    def crossed(self):
        if self.ycor() >= 300:
            return True
        else:
            return False
