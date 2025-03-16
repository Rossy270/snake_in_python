from turtle import Turtle

FONT = ("Arial", 16, "bold")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.show_text()

    def show_text(self):
       self.clear()
       self.write(f"Current Score: {self.score}", font= FONT, align= ALIGN)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", font= FONT, align= ALIGN)

    def increase_score(self):
        self.score += 1
        self.show_text()
