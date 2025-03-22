from turtle import Turtle

MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.head = None
        self.create_snake()


    def create_snake(self):
        for i in range(3):
            self.add_segment(i)

        self.head = self.segments[0]


    def extend(self):
        self.add_segment(len(self.segments))
        self.move()

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_FORWARD)

    def add_segment(self, segment_indices):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()

        current_xcor = new_turtle.xcor()
        current_xcor += segment_indices * -20

        new_turtle.setx(current_xcor)
        self.segments.append(new_turtle)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()