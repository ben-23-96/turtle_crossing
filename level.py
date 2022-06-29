from turtle import Turtle
import os


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('blue')
        self.high_level_path = os.path.dirname(__file__) + "\\high_level.txt"
        with open(self.high_level_path, "r") as reader:
            high_level = int(reader.read())
        self.high_level = high_level

    def next_level(self):
        self.level += 1

    def display_round(self):
        self.setposition((-300, 290))
        self.clear()
        self.write(f'Level {self.level}',
                   font=('comic sans', 20, 'bold'), align='center')
        self.setposition((260, 290))
        self.write(f"Highest Level: {self.high_level}", font=(
            'comic sans', 20, 'bold'), align='center')

    def game_over(self):
        self.setposition((0, 290))
        self.write(f'Game Over',
                   font=('comic sans', 20, 'bold'), align='center')
        if self.level > self.high_level:
            with open(self.high_level_path, "w") as writer:
                writer.write(f"{self.level}")
            self.high_level = self.level

    def new_game(self):
        self.level = 1
        self.clear()
        self.display_round()
