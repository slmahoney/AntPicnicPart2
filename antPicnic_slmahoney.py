
import pygame, simpleGE, random

"ant picnic"
"slide and catch game"
"Sabrina mahoney"

class Cookie(simpleGE.Sprite):
    def__init__(self,scene):
        super().__init__(scene)
        self.setImage("Cookie.png")
        self.setSize(25,25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        #move to top of screen
        self.y = 10
        
        #x is random 0 - screen width
        self.x = random.randint(0, self.screenWidth)
        
        #dy is random minSpeed to maxSpeed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class Ant(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ant.png")
        self.setSize(50,50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.y += self.moveSpeed
        
class LblScore(simpleGE.Label):
    def__init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100,30)
        
class LblTime(simpleGE.Label):
    def__init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500,30)
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("blanket.png")
        
        self.sndCookie = simpleGE.Sound("apple_bite.wav")
        self.numCookies = 10
        self.score = 0
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.lblTime = LblTime()
        self.lblScore = LblScore()
        self.ant = Ant(self)
        
        self.cookies = []
        for i in range(self.numCookies):
            self.cookies.append(Cookie(self))
        
        self.sprites = [self.ant,
                        self.cookie,
                        self.lblScore,
                        sel.lblTime]
        
    def process(self):
        for cookie in self.cookies:
        if cookie.collidesWith(self.cookie):
            cookie.reset()
            self.sndCookie.play()
            self.score += 1
            self.lblScore.text = f"Score: {self.score}"
            
            
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft().2f}
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()
            
class Instructions (simpleGE.Scene):
    def__init__(self, prevScore):
        super().__init__()
        
        self.prevScore = prevScore
        self.lblScore.text = f"Last score: {self.prevScore}"
        
        
        self.setImage("blanket.jpg")
        self.response = "Quit"
        
        
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
            "You are an ant",
            "Move with left and right arrow keys",
            "Eat as many cookies as you can",
            "in the time provided"]
        self.directions.center = (320,240)
        self.directions.size = (500,250)
        
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100,400)
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540,400)
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Last score: 0"
        self.lblScore.center = (320,400)
        
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
    
     

    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        
            
            

        
def main():
    
    keepGoing = True
    lastScore = 0
    
    while keepGoing:
    
    instructions = Instructions(lastScore)
    instructions = Instructions()
    instructions.start()
    
    
    
    if instructions.response == "Play":
    
    game = Game()
    game.start()
    lastScore = game.score
    
    else:
        keepGoing = False
    
if __name__=="__main__":
    main()