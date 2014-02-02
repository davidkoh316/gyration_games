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


class EntryScreen(State.State):
    FADEINTIME = .6
    FADEOUTTIME = .2

    def __init__(self):
        self.time = 0.0
        self.color = pygame.color.Color("black")
        Globals.SCREEN.fill(pygame.color.Color("black"))
        self.text = "Noel's Journey ... "
        self.width, self.height = Globals.FONT.size(self.text)
        AudioManager.loadSfxSet("title")
        if AudioManager.loadedMusic != "title" or\
                not pygame.mixer.music.get_busy():
            AudioManager.loadMusic("title")
            pygame.mixer.music.play(-1)
        ImageManager.loadSet("title")
        self.temp = ImageManager.levelRes["title"]["Title_Screen.png"]
        ImageManager.levelRes["title"]["Title_Screen.png"] =\
            pygame.transform.scale(self.temp, (1000, 600))

    def draw(self):
        self.temp = ImageManager.levelRes["title"]["Title_Screen.png"]
        Globals.SCREEN.blit(self.temp, (0, 0))
        self.text = "Noel's Journey ... "
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (200, 50))
        Globals.SCREEN.blit(self.temp, (50, 50))
        self.text = "Noel is determined to win back his town"
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 100))
        self.text = "from the evil snow monster. He must first"
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 140))
        self.text = "survive the whimsy forest, collect suns, and"
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 180))
        self.text = "defeat the happy, deadly creatures that reside."
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (300, 40))
        Globals.SCREEN.blit(self.temp, (100, 220))

    def update(self, time):
        if InputManager.getPressed("enter") or InputManager.getPressed("jump"):
            pygame.mixer.music.stop()
            Globals.CURRENT_LEVEL = "one"
            pygame.mixer.music.stop()
            Globals.STATE = GameScreen.GameScreen()
            return
        self.time += time
        if self.time < EntryScreen.FADEINTIME:
            ratio = self.time / EntryScreen.FADEINTIME
            #value = int(ratio * 255)
            #self.color = pygame.color.Color(value, value, value)
