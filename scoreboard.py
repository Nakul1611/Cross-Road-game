from turtle import Turtle

FONT = ("Courier", 24, "normal")
level = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-180, 250)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"level : {self.level}", align="left" , font = "FONT")
    
    def increase_level(self):
        self.level += 1 
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center" , font="FONT")





    
