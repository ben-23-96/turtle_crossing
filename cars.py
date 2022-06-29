from turtle import Turtle
from random import randint


class Car(Turtle):
    def __init__(self):
        super().__init__()

    def create_car(self):
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.setheading(180)
        self.setposition((350, randint(-275, 275)))
        self.color((randint(0, 255), randint(0, 255), randint(0, 255)))


class Traffic_control():
    def __init__(self):
        self.cars = []
        self.speed = 10
        self.car_volume = 8
        self.round = 1

    def new_cars(self):
        if randint(0, self.car_volume) == 2:
            new_car = Car()
            new_car.create_car()
            self.cars.append(new_car)

    def reset(self):
        for car in self.cars:
            car.clear()
            car.hideturtle()
        self.cars = []

    def drive(self):
        for car in self.cars:
            if car.xcor() > -425:
                car.forward(self.speed)

    def collison(self, player):
        for car in self.cars:
            if car.ycor() + 20 > player.ycor() and car.ycor() - 20 < player.ycor():
                if car.xcor() + 40 > player.xcor() and car.xcor() - 40 < player.xcor():
                    return True
        return False

    def difficulty_increase(self):
        self.speed += 2
        self.round += 1
        if self.round % 2 == 0:
            if self.car_volume > 2:
                self.car_volume -= 2

    def new_game(self):
        self.reset()
        self.round = 1
        self.speed = 10
        self.car_volume = 8
