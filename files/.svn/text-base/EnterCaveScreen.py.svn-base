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


class EnterCaveScreen(State.State):
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
        self.temp = ImageManager.levelRes["cutscene"]["CutScene2to3_1.png"]
        ImageManager.levelRes["cutscene"]["CutScene2to3_1.png"] =\
            pygame.transform.scale(self.temp, (800, 600))
        self.state = 0
        self.sceneTime = 0.0

    def draw(self):
        if self.state == 0:
            self.temp = ImageManager.levelRes["cutscene"]["CutScene2to3_1.png"]
        elif self.state == 1:
            self.temp = ImageManager.levelRes["cutscene"]["CutScene2to3_2.png"]
        elif self.state == 2:
            self.temp = ImageManager.levelRes["cutscene"]["CutScene2to3_3.png"]
        Globals.SCREEN.blit(self.temp, (0, 0))
        self.text = "Enter the cave ... "
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (200, 50))
        Globals.SCREEN.blit(self.temp, (50, 50))
        self.text = "Noel must travel through the deadly cave"
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 100))
        self.text = "to reach the other end of island."
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 140))
        self.text = "This will test his determination"
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 180))
        self.text = "and power against the darkness."
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 220))

    def update(self, time):
        if InputManager.getPressed("enter") or InputManager.getPressed("jump"):
            pygame.mixer.music.stop()
            Globals.STATE = GameScreen.GameScreen()
            return
        self.time += time
        if self.time < EnterCaveScreen.FADEINTIME:
            ratio = self.time / EnterCaveScreen.FADEINTIME
        if self.sceneTime > 1.0:
            self.state = (self.state + 1) % 3
            self.sceneTime = 0.0
        self.sceneTime += time
