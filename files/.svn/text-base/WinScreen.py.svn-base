# The Win screen

import InputManager
import State
import Globals
import GameScreen
import HighScoreInputScreen
import SkillScreen
import MapScreen
import EnterMountainScreen
import EnterCaveScreen
import EnterSnowScreen
import EnterFinalScreen
import AudioManager

import pygame.sprite
import pygame.image
import pygame.time
import pygame.mixer

import pygame.color


class WinScreen(State.State):
    FADEINTIME = 0.7
    FADEOUTTIME = 0.2

    def __init__(self):
        self.time = 0.0
        self.color = pygame.color.Color("black")
        self.selectedColor = pygame.color.Color("black")
        Globals.SCREEN.fill(pygame.color.Color("black"))
        self.temp = pygame.Surface((1, 1))
        self.selectionID = 1
        self.text = "LEVEL COMPLETE!"
        self.width, self.height = Globals.FONT.size(self.text)
        AudioManager.loadSfxSet("menu")
        Globals.LASTSCREENMAIN = False

    def draw(self):
        self.temp = Globals.FONT.render(self.text, True, (255, 255, 0))
        self.temp = pygame.transform.scale(self.temp, (500, 100))
        Globals.SCREEN.blit(self.temp, (150, 100))

        if self.selectionID == 0:
            temp = Globals.FONT.render("Continue", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Continue", True, self.color)
        width = 220
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (290, 270))

        if self.selectionID == 1:
            temp = Globals.FONT.render(
                "Select Skills", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Select Skills", True, self.color)
        width = 300
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (250, 330))

        if self.selectionID == 2:
            temp = Globals.FONT.render(
                "Choose Level", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Choose Level", True, self.color)
        width = 300
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (250, 380))

        if self.selectionID == 3:
            temp = Globals.FONT.render("Quit", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Quit", True, self.color)
        width = 110
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (350, 430))

    def enter_game(self):
        if Globals.CURRENT_LEVEL == "two":
            Globals.STATE = EnterMountainScreen.EnterMountainScreen()
        elif Globals.CURRENT_LEVEL == "three":
            Globals.STATE = EnterCaveScreen.EnterCaveScreen()
        elif Globals.CURRENT_LEVEL == "four":
            Globals.STATE = EnterSnowScreen.EnterSnowScreen()
        elif Globals.CURRENT_LEVEL == "five":
            Globals.STATE = EnterFinalScreen.EnterFinalScreen()
        self.time = 0

    def enter_main(self):
        Globals.STATE = HighScoreInputScreen.HighScoreInputScreen()

    def update(self, time):
        if InputManager.getPressed("up"):
            self.selectionID -= 1
            if self.selectionID < 0:
                self.selectionID = 3
            AudioManager.sounds["menu"]["menuSound.ogg"].play()
        elif InputManager.getPressed("down"):
            self.selectionID = (self.selectionID + 1) % 4
            AudioManager.sounds["menu"]["menuSound.ogg"].play()

        if InputManager.getPressed("enter"):
            AudioManager.sounds["menu"]["menuSound.ogg"].play()
            AudioManager.unloadSfxSet("menu")
            if self.selectionID == 0:
                self.enter_game()
            elif self.selectionID == 1:
                Globals.STATE = SkillScreen.SkillScreen()
            elif self.selectionID == 2:
                Globals.STATE = MapScreen.MapScreen()
            elif self.selectionID == 3:
                self.enter_main()
        self.time += time
        if self.time < WinScreen.FADEINTIME:
            ratio = self.time / WinScreen.FADEINTIME
            value = int(ratio * 255)
            halfValue = int(ratio * 127)
            self.color = pygame.color.Color(value, value, value)
            self.selectedColor =\
                pygame.color.Color(halfValue, value, halfValue)
