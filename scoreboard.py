from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 22, 'bold')

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,250)
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}",align=ALIGNMENT,font=FONT)

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt','w') as file:
                file.write(str(self.high_score))
        
        self.display_score()


    def reset_scoreboard(self):
        self.score = 0
        self.display_score()
