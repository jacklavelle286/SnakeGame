from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.write(f"Score:{self.starting_score}", move=False, align="center", font=("Courier", 14, "normal"))

    def update_scoreboard(self):
        self.write(f"Score:{self.starting_score}", move=False, align="center", font=("Courier", 14, "normal"))

    def increase_score(self):
        self.starting_score += 1
        self.clear()
        self.update_scoreboard()

    def end_game(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game over. Your score was {self.starting_score}.", move=False, align="center", font=("Courier", 14, "normal"))
        f = open("scoreboard.txt", "a")
        f.write(input("Enter your name: "))
        f.write(f": {self.starting_score}\n")
        f.seek(0, 2)

    def show_score(self):
        self.write



