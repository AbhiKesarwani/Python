from turtle import Turtle, Screen
import random

tom = Turtle()
tom.shape("arrow")
tom.speed(10)
tom.width(10)


screen = Screen()
screen.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r,g,b)
    return color_tuple

direction = [0,90,180,270]

for _ in range(200):
    tom.fd(30)
    tom.color(random_colour())
    tom.setheading(random.choice(direction))



screen.exitonclick()

