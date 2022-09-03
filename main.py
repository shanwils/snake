from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
POS_WALL = 295
NEG_WALL = -295
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > POS_WALL or snake.head.xcor() < NEG_WALL or \
            snake.head.ycor() > POS_WALL or snake.head.ycor() < NEG_WALL:
        game_is_on = False
        scoreboard.reset()
        snake.reset()
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.reset()
            snake.reset()
            scoreboard.game_over()

screen.exitonclick()
