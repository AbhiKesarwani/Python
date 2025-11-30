from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

score = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.movement_snake()
    snake.direction_snake()

    #Detect collision with food.
    if snake.segments[0].distance(food) < 15:
        food.referesh()
        score.increase_score()
        snake.extend()


    #Detect collision with wall.
    if snake.segments[0].xcor() >300 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300:
        game_is_on = False
        score.game_over()

    #Detect collision with tail...If first segment collides with any segment in the tail,then game is over.
    for segmented in snake.segments[1:]:
       if snake.segments[0].distance(segmented) < 10:
           game_is_on = False
           score.game_over()










screen.exitonclick()