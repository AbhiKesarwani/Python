from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=500, width=500)
colors = ["black", "blue", "red", "orange", "yellow"]
y_pos = [-70, -40, 40, 65, 88]
turtles = []

for i in range(0, 5):
    tom = Turtle()
    tom.penup()
    tom.shape("turtle")
    tom.color(colors[i])
    tom.goto(x=-230, y=y_pos[i])
    turtles.append(tom)

text_input = screen.textinput(title="BET TURTLE", prompt="Choose a turtle color?")

race_on = False

if text_input:
    race_on = True

while race_on:
    for t in turtles:
        dist = random.randint(0, 10)
        t.forward(dist)
        if t.xcor()>230:
            race_on=False
            winning_color = t.pencolor()
            if winning_color == text_input:
                print("YOU WON!")
            else:
                print("YOU LOST! HAAR GYE")


screen.exitonclick()
