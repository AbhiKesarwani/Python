from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forward():
    tom.fd(50)
def move_backward():
    tom.bk(50)

def move_counter_clockwise():
    tom.lt(50)

def move_clockwise():
    new_heading = tom.heading() - 50
    tom.setheading(new_heading)

def clear_home():
    tom.penup()
    tom.clear()
    tom.home()
    tom.pendown()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_counter_clockwise, key="a")
screen.onkey(fun=move_clockwise, key="d")
screen.onkey(fun=clear_home, key="c")




screen.exitonclick()