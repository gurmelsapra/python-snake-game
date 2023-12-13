from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.bgcolor("Black")
screen.tracer(0)

new_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.right, "Right")
screen.onkey(new_snake.left, "Left")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    new_snake.move()

    if new_snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        new_snake.extend()

    if new_snake.head.xcor() > 280 or new_snake.head.xcor() < -280 or new_snake.head.ycor() > 280 or new_snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
