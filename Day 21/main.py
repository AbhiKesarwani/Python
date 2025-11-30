from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

screen.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
score = Scoreboard()

ball = Ball()

screen.listen()
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_down()

    #colliseion with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 :
        ball.bounce_back()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_back()

    # missed the collision with paddle
    if ball.xcor() > 350:
            ball.reset_position()
            score.l_point()

    if ball.xcor() < -350:
            ball.reset_position()
            score.r_point()















screen.exitonclick()