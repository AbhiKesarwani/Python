from turtle import Turtle, Screen
MOVE_DISTANCE = 20
STARTING_POSITION = [(0,0),(-20,0),(20,0)]
screen = Screen()
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.speed("slowest")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def movement_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)


    def direction_snake(self):
        def snake_up():
            if self.segments[0].heading() != 270:
               self.segments[0].setheading(90)

        def snake_down():
            if self.segments[0].heading() != 90:
               self.segments[0].setheading(270)

        def snake_right():
            if self.segments[0].heading() != 180:
               self.segments[0].setheading(0)

        def snake_left():
            if self.segments[0].heading() != 0:
               self.segments[0].setheading(180)

        screen.listen()
        screen.onkey(snake_up, key="Up")
        screen.onkey(snake_down, key="Down")
        screen.onkey(snake_right, key="Right")
        screen.onkey(snake_left, key="Left")