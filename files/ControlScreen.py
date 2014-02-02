import InputManager
import State
import Globals
import GameScreen
import EntryScreen
import MainScreen
import AudioManager
import ImageManager
import SettingScreen

import pygame.sprite
import pygame.image
import pygame.time
import pygame.mixer

import pygame.color


class ControlScreen(State.State):
    FADEINTIME = 1.0
    FADEOUTTIME = 0.2

    def __init__(self):
        self.time = 0.0
        self.red = pygame.color.Color("red")
        self.yellow = pygame.color.Color("yellow")
        self.blue = pygame.color.Color("blue")
        self.white = pygame.color.Color("white")
        self.color = pygame.color.Color("black")
        self.selectedColor = pygame.color.Color("black")
        Globals.SCREEN.fill(pygame.color.Color("black"))
        self.selectionID = 0
        self.astoriaToggleTime = 0.0
        self.astoriaToggleTimeInterval = 2
        self.astoriaOpacity = 0
        self.skills = [
            Globals.SKILL_JUMP, Globals.SKILL_DAMAGE, Globals.SKILL_MAX_HEALTH]
        self.colorWheel = [self.blue, self.yellow, self.red]
        ImageManager.loadSet("effects")
        self.sunImage = ImageManager.levelRes["effects"]["sun.png"]
        ImageManager.levelRes["effects"]["sun.png"] =\
            pygame.transform.scale(self.sunImage, (50, 50))
        ImageManager.loadSet("player")
        self.playerWalk = ImageManager.levelRes["player"]["Noelwalk.png"]
        ImageManager.levelRes["player"]["Noelwalk.png"] =\
            pygame.transform.scale(self.playerWalk, (50, 75))
        self.playerJump = ImageManager.levelRes["player"]["noel_jump.png"]
        ImageManager.levelRes["player"]["noel_jump.png"] =\
            pygame.transform.scale(self.playerJump, (50, 75))
        self.attack = ImageManager.levelRes["player"]["NoelWithZord.png"]
        ImageManager.levelRes["player"]["NoelWithZord.png"] =\
            pygame.transform.scale(self.attack, (50, 75))
        self.arrow = ImageManager.levelRes["player"]["BowArrow.png"]
        ImageManager.levelRes["player"]["BowArrow.png"] =\
            pygame.transform.scale(self.arrow, (200, 150))
        self.zord = ImageManager.levelRes["player"]["zord.png"]
        ImageManager.levelRes["player"]["zord.png"] =\
            pygame.transform.scale(self.arrow, (50, 50))

    def draw(self):
        temp = Globals.FONT.render("OBJECTIVE", True, self.white)
        temp = pygame.transform.scale(temp, (200, 50))
        Globals.SCREEN.blit(temp, (300, 30))

        temp = Globals.FONT.render(
            "Noel's town of Astoria has been taken"
            + " over by an evil Snow Monster.", True, self.white)
        temp = pygame.transform.scale(temp, (700, 50))
        Globals.SCREEN.blit(temp, (50, 90))
        temp = Globals.FONT.render(
            "Noel must travel across the island of"
            + " Astoria to collect Mini Suns.", True, self.white)
        temp = pygame.transform.scale(temp, (700, 50))
        Globals.SCREEN.blit(temp, (50, 140))
        temp = Globals.FONT.render(
            "The Mini Suns give Noel the skills"
            + " to defeat the Snow Monster", True, self.white)
        temp = pygame.transform.scale(temp, (700, 50))
        Globals.SCREEN.blit(temp, (50, 190))
        temp = Globals.FONT.render(
            "by melting away the cold winter snow"
            + " to get back Astoria!", True, self.white)
        temp = pygame.transform.scale(temp, (700, 50))
        Globals.SCREEN.blit(temp, (50, 240))

        temp = Globals.FONT.render("CONTROLS", True, self.white)
        temp = pygame.transform.scale(temp, (200, 50))
        Globals.SCREEN.blit(temp, (300, 310))

        temp = Globals.FONT.render("Move", True, self.white)
        temp = pygame.transform.scale(temp, (75, 50))
        Globals.SCREEN.blit(temp, (30, 525))
        temp = Globals.FONT.render("Arrow Keys", True, self.white)
        temp = pygame.transform.scale(temp, (95, 30))
        Globals.SCREEN.blit(temp, (25, 490))
        Globals.SCREEN.blit(self.playerWalk, (40, 375))
        temp = Globals.FONT.render("Jump", True, self.blue)
        temp = pygame.transform.scale(temp, (75, 50))
        Globals.SCREEN.blit(temp, (150, 525))
        temp = Globals.FONT.render("Space Bar", True, self.blue)
        temp = pygame.transform.scale(temp, (85, 30))
        Globals.SCREEN.blit(temp, (150, 490))
        Globals.SCREEN.blit(self.playerJump, (160, 375))
        temp = Globals.FONT.render("Attack", True, self.yellow)
        temp = pygame.transform.scale(temp, (100, 50))
        Globals.SCREEN.blit(temp, (265, 525))
        temp = Globals.FONT.render("A button", True, self.yellow)
        temp = pygame.transform.scale(temp, (75, 30))
        Globals.SCREEN.blit(temp, (275, 490))
        Globals.SCREEN.blit(self.attack, (285, 375))
        temp = Globals.FONT.render("Sword", True, self.white)
        temp = pygame.transform.scale(temp, (100, 50))
        Globals.SCREEN.blit(temp, (390, 525))
        temp = Globals.FONT.render("1 button", True, self.white)
        temp = pygame.transform.scale(temp, (75, 30))
        Globals.SCREEN.blit(temp, (405, 490))
        Globals.SCREEN.blit(self.zord, (420, 400))
        temp = Globals.FONT.render("Arrows", True, self.red)
        temp = pygame.transform.scale(temp, (100, 50))
        Globals.SCREEN.blit(temp, (520, 525))
        temp = Globals.FONT.render("2 button", True, self.red)
        temp = pygame.transform.scale(temp, (75, 30))
        Globals.SCREEN.blit(temp, (535, 490))
        Globals.SCREEN.blit(self.arrow, (545, 410))
        temp = Globals.FONT.render("Mini Suns", True, self.yellow)
        temp = pygame.transform.scale(temp, (125, 50))
        Globals.SCREEN.blit(temp, (650, 525))
        temp = Globals.FONT.render("Collect Them All!", True, self.yellow)
        temp = pygame.transform.scale(temp, (125, 30))
        Globals.SCREEN.blit(temp, (650, 490))
        Globals.SCREEN.blit(self.sunImage, (680, 405))

    def update(self, time):
        if not Globals.LASTSCREENSETTING:
            if InputManager.getPressed("enter") or\
                    InputManager.getPressed("jump"):
                Globals.STATE = EntryScreen.EntryScreen()
            elif InputManager.getPressed("esc"):
                Globals.STATE = MainScreen.MainScreen()
        else:
            if InputManager.getPressed("enter") or\
                    InputManager.getPressed("jump") or\
                    InputManager.getPressed("esc"):
                Globals.STATE = SettingScreen.SettingScreen()
                Globals.LASTSCREENSETTING = False

        self.time += time
        if self.time < ControlScreen.FADEINTIME:
            ratio = self.time / ControlScreen.FADEINTIME
            value = int(ratio * 255)
            halfValue = int(ratio * 127)
            self.color = pygame.color.Color(value, value, value)
            self.selectedColor =\
                pygame.color.Color(halfValue, value, halfValue)
        self.astoriaToggleTime += time
        if self.astoriaToggleTime < self.astoriaToggleTimeInterval:
            ratio = self.astoriaToggleTime / self.astoriaToggleTimeInterval
            self.astoriaOpacity = int(ratio * 255)
        elif self.astoriaToggleTime < self.astoriaToggleTimeInterval * 2:
            ratio = self.astoriaToggleTime / self.astoriaToggleTimeInterval
            ratio = 1 -\
                (self.astoriaToggleTime - self.astoriaToggleTimeInterval) /\
                self.astoriaToggleTimeInterval
            self.astoriaOpacity = int(ratio * 255)
        else:
            self.astoriaToggleTime = 0
