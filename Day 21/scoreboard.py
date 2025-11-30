from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.scoreboard()

    def scoreboard(self):
        self.goto(150, 200)
        self.write(self.r_score,align = "center",font = ('Arial', 20, 'normal'))
        self.goto(-150, 200)
        self.write(self.l_score, align="center", font=('Arial', 20, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.scoreboard()