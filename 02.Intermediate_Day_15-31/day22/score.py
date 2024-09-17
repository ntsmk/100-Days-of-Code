from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0

    def add_score_r(self):
        self.score_r += 1
        #print(f"right score: {self.score_r}")

    def add_score_l(self):
        self.score_l += 1
        #print(f"left score: {self.score_l}")

