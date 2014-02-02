import InputManager
import State
import Globals
import GameScreen
import EntryScreen
import HighScoreScreen
import WinScreen
import SettingScreen
import MainScreen
import AudioManager
import ImageManager

import pygame.sprite
import pygame.image
import pygame.time
import pygame.mixer

import pygame.color


class SkillScreen(State.State):
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
        Globals.LASTSCREENMAIN = True
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

    def drawCircles(self):
        dist = 350
        for i in range(Globals.SKILL_JUMP):
            pygame.draw.circle(Globals.SCREEN, self.blue, (dist, 320), 20)
            dist = dist + 50
        dist = 350
        for j in range(Globals.SKILL_DAMAGE):
            pygame.draw.circle(Globals.SCREEN, self.yellow, (dist, 380), 20)
            dist = dist + 50
        dist = 350
        for k in range(Globals.SKILL_MAX_HEALTH):
            pygame.draw.circle(Globals.SCREEN, self.red, (dist, 440), 20)
            dist = dist + 50

        temp = Globals.FONT.render("MINI SUNS", True, self.yellow)
        temp = pygame.transform.scale(temp, (275, 75))
        Globals.SCREEN.blit(temp, (50, 200))
        dist = 350
        for sun in range(Globals.MINI_SUNS):
            #pygame.draw.circle(Globals.SCREEN, self.white, (dist, 200), 20)
            Globals.SCREEN.blit(self.sunImage, (dist, 200))
            dist = dist + 75

    def draw(self):
        self.drawCircles()

        temp = Globals.FONT.render("SKILLS", True, self.white)
        temp = pygame.transform.scale(temp, (400, 100))
        Globals.SCREEN.blit(temp, (225, 50))

        if self.selectionID == 0:
            temp = Globals.FONT.render("Jump", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Jump", True, self.white)
        width = 215
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (50, 300))

        if self.selectionID == 1:
            temp = Globals.FONT.render("Damage", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Damage", True, self.white)
        width = 215
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (50, 360))

        if self.selectionID == 2:
            temp = Globals.FONT.render("Health", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Health", True, self.white)
        width = 215
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (50, 420))

        if self.selectionID == 3:
            temp = Globals.FONT.render("Done", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Done", True, self.color)
        width = 215
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (50, 500))

    def enter_jump(self):
        if Globals.MINI_SUNS > 0 and Globals.SKILL_JUMP < Globals.MAX_SKILL:
            Globals.PLAYER_JUMP = Globals.PLAYER_JUMP + 20
            Globals.MINI_SUNS = Globals.MINI_SUNS - 1
            Globals.SKILL_JUMP = Globals.SKILL_JUMP + 1

    def enter_damage(self):
        if Globals.MINI_SUNS > 0 and Globals.SKILL_DAMAGE < Globals.MAX_SKILL:
            Globals.PLAYER_DAMAGE = Globals.PLAYER_DAMAGE + 2
            Globals.ARROW_DAMAGE = Globals.ARROW_DAMAGE + 2
            Globals.MINI_SUNS = Globals.MINI_SUNS - 1
            Globals.SKILL_DAMAGE = Globals.SKILL_DAMAGE + 1

    def enter_health(self):
        if Globals.MINI_SUNS > 0 and\
                Globals.SKILL_MAX_HEALTH < Globals.MAX_SKILL:
            Globals.PLAYER_MAX_HEALTH = Globals.PLAYER_MAX_HEALTH + 3
            Globals.MINI_SUNS = Globals.MINI_SUNS - 1
            Globals.SKILL_MAX_HEALTH = Globals.SKILL_MAX_HEALTH + 1

    def enter_done(self):
        Globals.STATE = WinScreen.WinScreen()

    def update(self, time):
        if InputManager.getPressed("up"):
            self.selectionID -= 1
            if self.selectionID < 0:
                self.selectionID = 3
            #AudioManager.sounds["menu"]["menuSound.ogg"].play()
        elif InputManager.getPressed("down"):
            self.selectionID = (self.selectionID + 1) % 4
            #AudioManager.sounds["menu"]["menuSound.ogg"].play()

        if InputManager.getPressed("enter"):
            #AudioManager.sounds["menu"]["menuSound.ogg"].play()
            AudioManager.unloadSfxSet("menu")
            if self.selectionID == 0:
                self.enter_jump()
            elif self.selectionID == 1:
                self.enter_damage()
            elif self.selectionID == 2:
                self.enter_health()
            elif self.selectionID == 3:
                self.enter_done()
        if InputManager.getPressed("esc"):
            self.enter_done()
        self.time += time
        if self.time < SkillScreen.FADEINTIME:
            ratio = self.time / SkillScreen.FADEINTIME
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
