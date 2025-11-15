from turtle import Turtle, Screen
import random

tom =Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

tom.shape("turtle")
tom.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.rt(5)

draw_spirograph(5)


screen.exitonclick()