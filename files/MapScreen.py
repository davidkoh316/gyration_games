import InputManager
import ImageManager
import State
import Globals
import PauseScreen
import MainScreen
import GameScreen
import EntryScreen
import EnterMountainScreen
import EnterCaveScreen
import EnterSnowScreen
import EnterFinalScreen
import WinScreen
import AudioManager
import ControllerSetupScreen
import World

import pygame.sprite
import pygame.image
import pygame.time
import pygame.mixer

import pygame.color


class MapScreen(State.State):
    FADEINTIME = 0.7
    FADEOUTTIME = 0.2

    def __init__(self):
        self.time = 0.0
        self.color = pygame.color.Color("black")
        self.selectedColor = pygame.color.Color("black")
        Globals.SCREEN.fill(pygame.color.Color("black"))
        #self.selectionID = 0
        self.currentLevel()
        AudioManager.loadSfxSet("menu")
        ImageManager.loadSet("map")
        self.temp =\
            ImageManager.levelRes["map"]["Astoria_Map_Grass_aftersnowboss.png"]
        ImageManager.levelRes["map"]["Astoria_Map_Grass_aftersnowboss.png"] =\
            pygame.transform.scale(self.temp, (800, 600))

    def currentLevel(self):
        if Globals.CURRENT_LEVEL is "one":
            self.selectionID = 0
        elif Globals.CURRENT_LEVEL is "two":
            self.selectionID = 1
        elif Globals.CURRENT_LEVEL is "three":
            self.selectionID = 2
        elif Globals.CURRENT_LEVEL is "four":
            self.selectionID = 3
        elif Globals.CURRENT_LEVEL is "five":
            self.selectionID = 4
        else:
            self.selectionID = 0

    def imageSelect(self):
        if Globals.LEVELS_BEAT == 0:
            text = "Astoria_Map_Grass_beforelvl1.png"
            self.temp = ImageManager.levelRes["map"][text]
            Globals.SCREEN.blit(self.temp, (0, 0))
        elif Globals.LEVELS_BEAT == 1:
            text = "Astoria_Map_Grass_beforelvl2.png"
            self.temp = ImageManager.levelRes["map"][text]
            Globals.SCREEN.blit(self.temp, (0, 0))
        elif Globals.LEVELS_BEAT == 2:
            text = "Astoria_Map_Grass_beforelvl3.png"
            self.temp = ImageManager.levelRes["map"][text]
            Globals.SCREEN.blit(self.temp, (0, 0))
        elif Globals.LEVELS_BEAT == 3:
            text = "Astoria_Map_Grass_beforelvl4.png"
            self.temp = ImageManager.levelRes["map"][text]
            Globals.SCREEN.blit(self.temp, (0, 0))
        elif Globals.LEVELS_BEAT == 4:
            text = "Astoria_Map_Grass_beforesnowboss.png"
            self.temp = ImageManager.levelRes["map"][text]
            Globals.SCREEN.blit(self.temp, (0, 0))
        elif Globals.LEVELS_BEAT == 5:
            text = "Astoria_Map_Grass_aftersnowboss.png"
            self.temp = ImageManager.levelRes["map"][text]
            Globals.SCREEN.blit(self.temp, (0, 0))

    def draw(self):
        self.imageSelect()

        if self.selectionID == 0:
            temp = Globals.FONT.render(
                "Forest Level", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Forest Level", True, self.color)
        width = 80
        height = 20
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (20, 350))

        if self.selectionID == 1:
            temp = Globals.FONT.render(
                "Mountain Level", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Mountain Level", True, self.color)
        width = 100
        height = 20
        temp = pygame.transform.scale(temp, (width, height))
        if Globals.LEVELS_BEAT > 0:
            Globals.SCREEN.blit(temp, (250, 275))

        if self.selectionID == 2:
            temp = Globals.FONT.render(
                "Cave Level", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Cave Level", True, self.color)
        width = 80
        height = 20
        temp = pygame.transform.scale(temp, (width, height))
        if Globals.LEVELS_BEAT > 1:
            Globals.SCREEN.blit(temp, (385, 190))

        if self.selectionID == 3:
            temp = Globals.FONT.render("Snow Level", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Snow Level", True, self.color)
        width = 80
        height = 20
        temp = pygame.transform.scale(temp, (width, height))
        if Globals.LEVELS_BEAT > 2:
            Globals.SCREEN.blit(temp, (605, 280))

        if self.selectionID == 4:
            temp = Globals.FONT.render("Boss Level", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Boss Level", True, self.color)
        width = 80
        height = 20
        temp = pygame.transform.scale(temp, (width, height))
        if Globals.LEVELS_BEAT > 3:
            Globals.SCREEN.blit(temp, (295, 505))

        if self.selectionID == (Globals.LEVELS_BEAT + 1):
            temp = Globals.FONT.render("Back", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Back", True, self.color)
        width = 50
        height = 20
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (700, 550))

    def enter_back(self):
        if Globals.GAMECOMPLETED:
            Globals.STATE = MainScreen.MainScreen()
        else:
            if Globals.LASTSCREENPAUSE:
                Globals.LASTSCREENPAUSE = False
                Globals.STATE = PauseScreen.PauseScreen()
            else:
                Globals.STATE = WinScreen.WinScreen()

    def update(self, time):
        if InputManager.getPressed("up"):
            self.selectionID -= 1
            if self.selectionID < 0:
                self.selectionID = (Globals.LEVELS_BEAT + 1)
        elif InputManager.getPressed("down"):
            self.selectionID =\
                (self.selectionID + 1) % (Globals.LEVELS_BEAT + 2)

        if InputManager.getPressed("enter"):
            if self.selectionID == 0:
                World.cleanupCompletely()
                Globals.PLAYER = None
                Globals.STATE = EntryScreen.EntryScreen()
                Globals.CURRENT_LEVEL = "one"
            elif self.selectionID == 1 and Globals.LEVELS_BEAT > 0:
                World.cleanupCompletely()
                Globals.PLAYER = None
                Globals.STATE = EnterMountainScreen.EnterMountainScreen()
                Globals.CURRENT_LEVEL = "two"
            elif self.selectionID == 2 and Globals.LEVELS_BEAT > 1:
                World.cleanupCompletely()
                Globals.PLAYER = None
                Globals.STATE = EnterCaveScreen.EnterCaveScreen()
                Globals.CURRENT_LEVEL = "three"
            elif self.selectionID == 3 and Globals.LEVELS_BEAT > 2:
                World.cleanupCompletely()
                Globals.PLAYER = None
                Globals.STATE = EnterSnowScreen.EnterSnowScreen()
                Globals.CURRENT_LEVEL = "four"
            elif self.selectionID == 4 and Globals.LEVELS_BEAT > 3:
                World.cleanupCompletely()
                Globals.PLAYER = None
                Globals.STATE = EnterFinalScreen.EnterFinalScreen()
                Globals.CURRENT_LEVEL = "five"
            elif self.selectionID == (Globals.LEVELS_BEAT + 1):
                self.enter_back()
        if InputManager.getPressed("esc"):
            self.enter_back()
        self.time += time
        if self.time < MapScreen.FADEINTIME:
            ratio = self.time / MapScreen.FADEINTIME
            value = int(ratio * 255)
            halfValue = int(ratio * 127)
            self.color = pygame.color.Color(value, value, value)
            self.selectedColor =\
                pygame.color.Color(halfValue, value, halfValue)
