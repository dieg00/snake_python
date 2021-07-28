from snake import Snake
from turtle import Screen, onkey
from food import Food
from scoreboard import Scoreboard
import time

def wait():
    time.sleep(30)
screen = Screen()
screen.setup(height=600, width=720)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
onkey(fun=snake.up, key="Up")
onkey(fun=snake.down, key="Down")
onkey(fun=snake.right, key="Right")
onkey(fun=snake.left, key="Left")

game_on = True

onkey(fun=wait, key="c")

while game_on:
    # print(snake.snake[1].pos())
    snake.move()
    if snake.snake[1].pos() == food.pos():
        food.change_position()
        scoreboard.add_point()
        snake.add_block()
    if snake.collided():
        game_on = False
        scoreboard.game_over()
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
