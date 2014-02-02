# HighScore Screen
import InputManager
import State
import Globals
import MainScreen
import AudioManager
import PauseScreen

import pygame.sprite
import pygame.image
import pygame.time
import pygame.mixer

import pygame.color


class HighScoreScreen(State.State):
    FADEINTIME = .6
    FADEOUTTIME = .2

    def addScores(self):
        file = open("highScores.txt")
        for line in file:
            name, x, score = line.partition(" ")
            score = int(score[:-1])
            self.hs[score] = name

    def __init__(self):
        self.time = 0.0
        self.color = pygame.color.Color("black")
        Globals.SCREEN.fill(pygame.color.Color("black"))
        self.temp = pygame.Surface((1, 1))
        self.text = "HIGH SCORES"
        self.width, self.height = Globals.FONT.size(self.text)
        AudioManager.loadSfxSet("title")
        self.hs = {}
        #self.playOnce = False
        self.addScores()

    def exit_title(self):
        if Globals.LASTSCREENMAIN or Globals.PLAYER is None:
            Globals.STATE = MainScreen.MainScreen()
        else:
            Globals.STATE = PauseScreen.PauseScreen()
        AudioManager.unloadSfxSet("title")

    def draw(self):
        self.temp = Globals.FONT.render(self.text, True, self.color)
        self.temp = pygame.transform.scale(self.temp, (400, 100))
        Globals.SCREEN.blit(self.temp, (200, 50))

        printout = 0
        spacing = 180
        for score in sorted(self.hs.iterkeys(), reverse=True):
            if printout < 10:
                self.temp = Globals.FONT.render(
                    self.hs[score] + "   " + str(score), True, self.color)
                self.temp = pygame.transform.scale(self.temp, (200, 35))
                Globals.SCREEN.blit(self.temp, (300, spacing))
                spacing = spacing + 40
            printout += 1

    def update(self, time):
        if InputManager.getPressed("esc") or\
                InputManager.getPressed("enter") or\
                InputManager.getPressed("jump"):
            self.exit_title()
            return
        self.time += time
        if self.time < HighScoreScreen.FADEINTIME:
            ratio = self.time / HighScoreScreen.FADEINTIME
            value = int(ratio * 255)
            self.color = pygame.color.Color(value, value, value)
