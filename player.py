from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(0, -280)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_player_at_finish_line(self):
        if self.distance(0, 270) < 10:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(0, -280)

