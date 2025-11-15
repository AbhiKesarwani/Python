from turtle import Turtle, Screen

tom = Turtle()
tom.shape("arrow")

colors=["DeepSkyBlue2","firebrick","ForestGreen","gold","gray0","green","hotpink","navy"]
num_side=3
while num_side<11:
    for _ in range(0,num_side):
        tom.color(colors[num_side-3])
        tom.fd(100)
        tom.rt(360/num_side)
    num_side += 1









screen = Screen()
screen.exitonclick()