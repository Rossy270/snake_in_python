from turtle import Turtle

FONT = ("Arial", 16, "bold")
ALIGN = "center"

def get_high_score():
    high_score = 0
    with open("data.txt") as file:
        high_score = int(file.read())

    return high_score

def update_high_score(current_high_score):
    with open("data.txt", mode="w") as file:
        file.write(str(current_high_score))

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.show_text()

    def show_text(self):
       self.clear()
       self.write(f"Score: {self.score} High Score: {self.high_score}", font= FONT, align= ALIGN)

    def reset(self):
        if self.score > self.high_score:
            self.high_score  = self.score

        update_high_score(self.high_score)
        self.score = 0
        self.show_text()

    def increase_score(self):
        self.score += 1
        self.show_text()
