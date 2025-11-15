from turtle import Turtle, Screen
tom = Turtle()


for _ in range(10):
    tom.pendown()
    tom.fd(10)
    tom.penup()
    tom.fd(10)

screen = Screen()
screen.exitonclick()