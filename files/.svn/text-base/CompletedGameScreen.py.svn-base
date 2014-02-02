import InputManager
import State
import Globals
import HighScoreInputScreen
import AudioManager
import ImageManager
import pygame.sprite
import pygame.image
import pygame.time
import pygame.mixer
import pygame.color


class CompletedGameScreen(State.State):
    FADEINTIME = .6
    FADEOUTTIME = .2

    def __init__(self):
        self.time = 0.0
        self.color = pygame.color.Color("white")
        AudioManager.loadSfxSet("title")
        ImageManager.loadSet("cutscene")
        self.temp = ImageManager.levelRes["cutscene"]["YOUWIN.png"]
        self.state = 0
        self.sceneTime = 0.0

    def draw(self):
        if self.state == 0:
            self.temp = ImageManager.levelRes["cutscene"]["YOUWIN.png"]
        elif self.state == 1:
            self.temp = ImageManager.levelRes["cutscene"]["YOUWIN2.png"]
        Globals.SCREEN.blit(self.temp, (-90, 0))
        self.temp = "Noel defeated the Snow Boss!"
        renderText = Globals.FONT.render(self.temp, True, self.color)
        self.temp = pygame.transform.scale(renderText, (600, 100))
        Globals.SCREEN.blit(self.temp, (100, 200))

    def update(self, time):
        if InputManager.getPressed("enter") or InputManager.getPressed("jump"):
            #pygame.mixer.music.fadeout(1000)
            Globals.STATE = HighScoreInputScreen.HighScoreInputScreen()
            return
        self.time += time
        if self.time < CompletedGameScreen.FADEINTIME:
            ratio = self.time / CompletedGameScreen.FADEINTIME
        if self.sceneTime > 1.0:
            self.state = (self.state + 1) % 2
            self.sceneTime = 0.0
        self.sceneTime += time
