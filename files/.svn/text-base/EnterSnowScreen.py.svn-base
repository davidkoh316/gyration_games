import InputManager
import State
import Globals
import GameScreen
import AudioManager
import ImageManager
import pygame.sprite
import pygame.image
import pygame.time
import pygame.mixer
import pygame.color


class EnterSnowScreen(State.State):
    FADEINTIME = .6
    FADEOUTTIME = .2

    def __init__(self):
        self.time = 0.0
        self.color = pygame.color.Color("white")
        Globals.SCREEN.fill(pygame.color.Color("black"))
        self.text = ""
        self.width, self.height = Globals.FONT.size(self.text)
        AudioManager.loadSfxSet("title")
        if AudioManager.loadedMusic != "title" or\
                not pygame.mixer.music.get_busy():
            AudioManager.loadMusic("title")
            pygame.mixer.music.play(-1)
        ImageManager.loadSet("cutscene")
        self.temp = ImageManager.levelRes["cutscene"]["CutScene3to4_1.png"]
        ImageManager.levelRes["cutscene"]["CutScene3to4_1.png"] =\
            pygame.transform.scale(self.temp, (800, 600))
        self.state = 0
        self.sceneTime = 0.0

    def draw(self):
        if self.state == 0:
            self.temp = ImageManager.levelRes["cutscene"]["CutScene3to4_1.png"]
        elif self.state == 1:
            self.temp = ImageManager.levelRes["cutscene"]["CutScene3to4_2.png"]
        Globals.SCREEN.blit(self.temp, (0, 0))
        self.text = "Embrace the snow ... "
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (200, 50))
        Globals.SCREEN.blit(self.temp, (50, 50))
        self.text = "Noel has passed through the cave only"
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 100))
        self.text = "to find himself in a white winter snow."
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 140))
        self.text = "Noel must use his warming powers"
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 180))
        self.text = "to get through the icy snow."
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 220))

    def update(self, time):
        if InputManager.getPressed("enter") or InputManager.getPressed("jump"):
            pygame.mixer.music.stop()
            Globals.STATE = GameScreen.GameScreen()
            return
        self.time += time
        if self.time < EnterSnowScreen.FADEINTIME:
            ratio = self.time / EnterSnowScreen.FADEINTIME
        if self.sceneTime > 2.0:
            self.state = (self.state + 1) % 2
            self.sceneTime = 0.0
        self.sceneTime += time
