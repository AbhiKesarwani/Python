from turtle import Turtle, Screen

tom = Turtle()

for _ in range(4):
    tom.fd(100)
    tom.rt(90)

screen = Screen()
screen.exitonclick()
