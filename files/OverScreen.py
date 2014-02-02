# The Game Over screen

import InputManager
import State
import Globals
import GameScreen
import HighScoreInputScreen
import AudioManager

import pygame.sprite
import pygame.image
import pygame.time
import pygame.mixer

import pygame.color


class OverScreen(State.State):
    FADEINTIME = 0.7
    FADEOUTTIME = 0.2

    def __init__(self):
        self.time = 0.0
        self.color = pygame.color.Color("black")
        self.selectedColor = pygame.color.Color("black")
        Globals.SCREEN.fill(pygame.color.Color("black"))
        self.temp = pygame.Surface((1, 1))
        self.selectionID = 0
        self.text = "GAME OVER"
        self.width, self.height = Globals.FONT.size(self.text)
        AudioManager.loadSfxSet("menu")
        Globals.LASTSCREENMAIN = False

    def draw(self):
        self.temp = Globals.FONT.render(self.text, True, self.color)
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
            temp = Globals.FONT.render("Quit", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Quit", True, self.color)
        width = 110
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (350, 330))

    def enter_game(self):
        Globals.STATE = GameScreen.GameScreen()
        self.time = 0

    def enter_main(self):
        Globals.STATE = HighScoreInputScreen.HighScoreInputScreen()

    def update(self, time):
        if InputManager.getPressed("up"):
            self.selectionID -= 1
            if self.selectionID < 0:
                self.selectionID = 1
            AudioManager.sounds["menu"]["menuSound.ogg"].play()
        elif InputManager.getPressed("down"):
            self.selectionID = (self.selectionID + 1) % 2
            AudioManager.sounds["menu"]["menuSound.ogg"].play()

        if InputManager.getPressed("enter"):
            AudioManager.sounds["menu"]["menuSound.ogg"].play()
            AudioManager.unloadSfxSet("menu")
            if self.selectionID == 0:
                self.enter_game()
            elif self.selectionID == 1:
                self.enter_main()
        self.time += time
        if self.time < OverScreen.FADEINTIME:
            ratio = self.time / OverScreen.FADEINTIME
            value = int(ratio * 255)
            halfValue = int(ratio * 127)
            self.color = pygame.color.Color(value, value, value)
            self.selectedColor =\
                pygame.color.Color(halfValue, value, halfValue)
