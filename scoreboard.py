from turtle import Turtle
from car_manager import CarManager

FONT1 = ("Courier", 24, "normal")
FONT2 = ("Courier", 14, "normal")
car_manager = CarManager()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT1)

    def level_up(self):
        self.level += 1
        self.goto(-270, 270)
        self.clear()
        self.write(f"Level : {self.level}", font=FONT2)
