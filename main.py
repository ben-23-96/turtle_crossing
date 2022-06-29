from turtle import Screen, done
import time
from player_turtle import Player_turtle
from cars import Traffic_control
from level import Level

screen = Screen()
screen.tracer(0)
screen.colormode(255)

player = Player_turtle()
player.start()
traffic = Traffic_control()
level = Level()

screen.onkeypress(player.move, 'space')

level.display_round()

game_finished = False
game_over = False

while not game_finished:

    screen.listen()
    screen.update()
    time.sleep(0.1)

    traffic.drive()

    traffic.new_cars()

    if game_over:
        new_game = screen.textinput(
            "New Game", "Type yes or no for new game:  ")
        if new_game == 'yes':
            traffic.new_game()
            player.start()
            level.new_game()
            game_over = False
        else:
            game_finished = True

    if player.crossed():
        traffic.reset()
        traffic.difficulty_increase()
        player.start()
        level.next_level()
        level.display_round()

    if traffic.collison(player):
        level.game_over()
        game_over = True


done()
