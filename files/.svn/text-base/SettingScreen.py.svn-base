# The SettingScreen screen

import InputManager
import State
import Globals
import PauseScreen
import MainScreen
import AudioManager
import ControllerSetupScreen
import ControlScreen
import Globals

import pygame.sprite
import pygame.image
import pygame.time
import pygame.mixer

import pygame.color


class SettingScreen(State.State):
    FADEINTIME = 0.7
    FADEOUTTIME = 0.2

    def __init__(self):
        self.time = 0.0
        self.color = pygame.color.Color("black")
        self.selectedColor = pygame.color.Color("black")
        Globals.SCREEN.fill(pygame.color.Color("black"))
        self.selectionID = 0
        AudioManager.loadSfxSet("menu")

    def draw(self):
        #if self.selectionID == 0:
        #    temp = Globals.FONT.render(
        #        "Adjust Brightness", True, self.selectedColor)
        #else:
        #    temp = Globals.FONT.render("Adjust Brightness", True, self.color)
        #width = 390
        #height = 50
        #temp = pygame.transform.scale(temp, (width, height))
        #Globals.SCREEN.blit(temp, (200, 120))

        #if self.selectionID == 1:
        #    temp = Globals.FONT.render(
        #        "Adjust Audio", True, self.selectedColor)
        #else:
        #    temp = Globals.FONT.render("Adjust Audio", True, self.color)
        #width = 260
        #height = 50
        #temp = pygame.transform.scale(temp, (width, height))
        #Globals.SCREEN.blit(temp, (270, 180))

        if self.selectionID == 0:
            temp = Globals.FONT.render(
                "Controller Setup", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Controller Setup", True, self.color)
        width = 400
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (200, 200))

        if self.selectionID == 1:
            temp = Globals.FONT.render(
                "Keyboard Controls", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Keyboard Controls", True, self.color)
        width = 400
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (200, 260))

        if self.selectionID == 2:
            temp = Globals.FONT.render("Back", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Back", True, self.color)
        width = 100
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (350, 320))

    def enter_brightness(self):
        Globals.STATE = BrightnessScreen.BrightnessScreen()

    def enter_volume(self):
        Globals.STATE = VolumeScreen.VolumeScreen()

    def enter_back(self):
        if Globals.LASTSCREENMAIN:
            Globals.STATE = MainScreen.MainScreen()
        else:
            Globals.STATE = PauseScreen.PauseScreen()

    def enter_csetup(self):
        Globals.STATE = ControllerSetupScreen.ControllerSetupScreen()

    def update(self, time):
        if InputManager.getPressed("up"):
            self.selectionID -= 1
            if self.selectionID < 0:
                self.selectionID = 2
            AudioManager.sounds["menu"]["menuSound.ogg"].play()
        elif InputManager.getPressed("down"):
            self.selectionID = (self.selectionID + 1) % 3
            AudioManager.sounds["menu"]["menuSound.ogg"].play()

        if InputManager.getPressed("enter"):
            AudioManager.sounds["menu"]["menuSound.ogg"].play()
            AudioManager.unloadSfxSet("menu")
            if self.selectionID == 0:
                self.enter_csetup()
            elif self.selectionID == 1:
                Globals.LASTSCREENSETTING = True
                Globals.STATE = ControlScreen.ControlScreen()
            elif self.selectionID == 2:
                self.enter_back()
        if InputManager.getPressed("esc"):
            self.enter_back()
        self.time += time
        if self.time < SettingScreen.FADEINTIME:
            ratio = self.time / SettingScreen.FADEINTIME
            value = int(ratio * 255)
            halfValue = int(ratio * 127)
            self.color = pygame.color.Color(value, value, value)
            self.selectedColor =\
                pygame.color.Color(halfValue, value, halfValue)
