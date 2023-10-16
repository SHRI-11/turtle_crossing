import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.setup(width=600, height=600)
screen.listen()
screen.onkeypress(player.move, "Up")
score_board.level_up()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.spawn_car()
    car_manager.move()
    screen.update()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car.xcor(), car.ycor()) < 20:
            game_is_on = False
            score_board.game_over()

    # Level up
    if player.is_player_at_finish_line():
        score_board.level_up()
        player.goto_start()
        car_manager.increase_speed()


screen.exitonclick()
screen.mainloop()
