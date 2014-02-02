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


class EnterFinalScreen(State.State):
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
        self.temp = ImageManager.levelRes["cutscene"]["CutSceneSnowboss.png"]
        ImageManager.levelRes["cutscene"]["CutSceneSnowboss.png"] =\
            pygame.transform.scale(self.temp, (800, 600))

    def draw(self):
        self.temp = ImageManager.levelRes["cutscene"]["CutSceneSnowboss.png"]
        Globals.SCREEN.blit(self.temp, (0, 0))
        self.text = "The final battle ... "
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (200, 50))
        Globals.SCREEN.blit(self.temp, (50, 50))
        self.text = "Noel must use his determination"
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 100))
        self.text = "and the power of the sun to"
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 140))
        self.text = "beat the evil Snow Monster."
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 180))
        self.text = "Noel must defeat him!"
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 220))

    def update(self, time):
        if InputManager.getPressed("enter") or InputManager.getPressed("jump"):
            pygame.mixer.music.stop()
            Globals.STATE = GameScreen.GameScreen()
            return
        self.time += time
        if self.time < EnterFinalScreen.FADEINTIME:
            ratio = self.time / EnterFinalScreen.FADEINTIME
