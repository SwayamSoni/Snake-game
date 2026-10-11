from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 12, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        file = open("snake_score.txt")
        self.high_score = int(file.read())
        file.close()
        self.color("white")
        self.hideturtle()
        self.teleport(0,280)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align=ALIGN, font=FONT)


    # def game_over(self):
    #     self.teleport(0,0)
    #     self.write("Game Over", False, align=ALIGN, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("snake_score.txt", mode='w')
            file.write(str(self.score))
            file.close()
        self.score = -1
        self.update_score()
    def update_score(self):
        self.score += 1
        self.clear()

        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align = ALIGN,font= FONT)
