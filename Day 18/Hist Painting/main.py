import colorgram

# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
# print(rgb_colors)


color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

import random

from turtle import Turtle, Screen
tom = Turtle()
screen = Screen()

screen.colormode(255)
tom.speed("fastest")
tom.penup()
tom.setheading(230)
tom.fd(250)
tom.setheading(0)
tom.hideturtle()


def movement():
    for i in range(10):
        tom.color(color_list[random.randint(0,29)])
        tom.pendown()
        tom.dot(20)
        tom.penup()
        tom.fd(50)
    tom.lt(90)
    tom.fd(40)
    tom.lt(90)
    tom.fd(500)
    tom.setheading(0)


for i in range(10):
    movement()


screen = Screen()
screen.exitonclick()



''' Circle code 
#import colorgram

#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)
#
#print(rgb_colors)

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

from turtle import Turtle, Screen
import random

tom = Turtle()
screen = Screen()
screen.colormode(255)
tom.speed("fast")
tom.penup()
tom.setheading(225)
tom.forward(400)
tom.setheading(0)

def movement():
    for _ in range(0,10):
        tom.pendown()
        tom.fillcolor(random.choice(color_list))
        tom.begin_fill()
        tom.circle(20)
        tom.end_fill()
        tom.penup()
        tom.fd(50)
        tom.color(random.choice(color_list))



movement()

for _ in range(0,4):
    tom.lt(90)
    tom.fd(100)
    tom.lt(90)
    tom.fd(50)
    movement()

    tom.rt(90)
    tom.fd(20)
    tom.rt(90)
    tom.fd(50)
    movement()

tom.lt(90)
tom.fd(100)
tom.lt(90)
tom.fd(50)
movement()

tom.hideturtle()

screen.exitonclick()

'''