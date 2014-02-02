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


class EnterMountainScreen(State.State):
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
        self.temp = ImageManager.levelRes["cutscene"]["CutSceneMountain.png"]
        ImageManager.levelRes["cutscene"]["CutSceneMountain.png"] =\
            pygame.transform.scale(self.temp, (800, 600))

    def draw(self):
        self.temp = ImageManager.levelRes["cutscene"]["CutSceneMountain.png"]
        Globals.SCREEN.blit(self.temp, (0, 0))
        self.text = "Scale the moutain ... "
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (200, 50))
        Globals.SCREEN.blit(self.temp, (50, 50))
        self.text = "Noel must climb the rough rocks"
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 100))
        self.text = "to get to the top of the mountain."
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 140))
        self.text = "Only upon success will he have any"
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 180))
        self.text = "hope to save his town of Astoria."
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 220))

    def update(self, time):
        if InputManager.getPressed("enter") or InputManager.getPressed("jump"):
            pygame.mixer.music.stop()
            Globals.STATE = GameScreen.GameScreen()
            return
        self.time += time
        if self.time < EnterMountainScreen.FADEINTIME:
            ratio = self.time / EnterMountainScreen.FADEINTIME
