from turtle import Turtle,Screen
screen = Screen()


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)


    def go_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(x=self.xcor(),y=new_y_cor)

    def go_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y_cor)



