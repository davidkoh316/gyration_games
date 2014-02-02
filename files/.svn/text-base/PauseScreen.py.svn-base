# The PauseScreen screen

import InputManager
import State
import Globals
import GameScreen
import MainScreen
import MapScreen
import SettingScreen
import AudioManager
import HighScoreScreen

import pygame.sprite
import pygame.image
import pygame.time
import pygame.mixer

import pygame.color


class PauseScreen(State.State):
    FADEINTIME = 0.7
    FADEOUTTIME = 0.2

    def __init__(self):
        self.time = 0.0
        self.color = pygame.color.Color("black")
        self.selectedColor = pygame.color.Color("black")
        Globals.SCREEN.fill(pygame.color.Color("black"))
        self.selectionID = 0
        AudioManager.loadSfxSet("menu")
        Globals.LASTSCREENMAIN = False
        Globals.LASTSCREENPAUSE = True

    def draw(self):
        if self.selectionID == 0:
            temp = Globals.FONT.render("Continue", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Continue", True, self.color)
        width = 220
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (290, 120))

        if self.selectionID == 1:
            temp =\
                Globals.FONT.render("Choose Level", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Choose Level", True, self.color)
        width = 260
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (270, 180))

        if self.selectionID == 2:
            temp = Globals.FONT.render("High Scores", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("High Scores", True, self.color)
        width = 260
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (270, 240))

        if self.selectionID == 3:
            temp = Globals.FONT.render("Settings", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Settings", True, self.color)
        width = 240
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (280, 300))

        if self.selectionID == 4:
            temp = Globals.FONT.render("Main Menu", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Main Menu", True, self.color)
        width = 240
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (275, 360))

        if self.selectionID == 5:
            temp = Globals.FONT.render("Exit Game", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Exit Game", True, self.color)
        width = 240
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (280, 420))

    def enter_game(self):
        Globals.STATE = GameScreen.GameScreen()
        self.time = 0

    def enter_map(self):
        Globals.LASTSCREENPAUSE = True
        Globals.STATE = MapScreen.MapScreen()

    def enter_highscore(self):
        Globals.STATE = HighScoreScreen.HighScoreScreen()

    def enter_main(self):
        Globals.STATE = MainScreen.MainScreen()

    def enter_settings(self):
        Globals.STATE = SettingScreen.SettingScreen()

    def exit_game(self):
        Globals.RUNNING = False

    def update(self, time):
        if InputManager.getPressed("up"):
            self.selectionID -= 1
            if self.selectionID < 0:
                self.selectionID = 5
            AudioManager.sounds["menu"]["menuSound.ogg"].play()
        elif InputManager.getPressed("down"):
            self.selectionID = (self.selectionID + 1) % 6
            AudioManager.sounds["menu"]["menuSound.ogg"].play()

        if InputManager.getPressed("enter"):
            AudioManager.sounds["menu"]["menuSound.ogg"].play()
            AudioManager.unloadSfxSet("menu")
            if self.selectionID == 0:
                self.enter_game()
            elif self.selectionID == 1:
                self.enter_map()
            elif self.selectionID == 2:
                self.enter_highscore()
            elif self.selectionID == 3:
                self.enter_settings()
            elif self.selectionID == 4:
                self.enter_main()
            elif self.selectionID == 5:
                self.exit_game()
        if InputManager.getPressed("esc"):
            self.enter_game()
        self.time += time
        if self.time < PauseScreen.FADEINTIME:
            ratio = self.time / PauseScreen.FADEINTIME
            value = int(ratio * 255)
            halfValue = int(ratio * 127)
            self.color = pygame.color.Color(value, value, value)
            self.selectedColor =\
                pygame.color.Color(halfValue, value, halfValue)
