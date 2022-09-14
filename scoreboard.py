from turtle import Turtle
MOVE = True
ALIGN = "center"
FONT = ("Arial", 12, "normal")
with open("data.txt") as file:
    contents = file.read()
    

class Scoreboard(Turtle):
    
    def __init__(self):

        super().__init__()
        self.penup()
        self.score = 0
        self.high_score = int(contents)
        self.color("white")
        self.hideturtle()
        self.refreshscore()

    def refreshscore(self):
        self.goto(0, 280)
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', True, align = "center", font = ("Arial", 12, "normal"))

    def reset(self):
        
        if self.score > self.high_score:
            
            self.high_score = self.score
            with open("data.txt", mode = "w") as file:
                file.write(f"{self.high_score}")
            
        self.score = 0
        self.refreshscore()


    def increase_score(self):
        self.score += 1
        self.refreshscore()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", True, align = "center", font = ("Arial", 18, "normal"))




