from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(-280, 240)
        self.update_scoreboard("")

    def update_scoreboard(self, game_status):
        self.clear()
        print(f"update score {self.score}")

        self.write(f"{game_status}Score : {self.score}", align="left", font=FONT)

