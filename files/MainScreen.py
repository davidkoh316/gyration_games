# The MainScreen screen

import InputManager
import State
import Globals
import GameScreen
import ControlScreen
import EntryScreen
import HighScoreScreen
import SettingScreen
import MapScreen
import AudioManager
import ImageManager
import World

import pygame.sprite
import pygame.image
import pygame.time
import pygame.mixer

import pygame.color


def transparentHack(bg, image, location, opacity):
    temp = pygame.Surface((image.get_width(), image.get_height()))
    temp.blit(bg, (-location[0], -location[1]))
    temp.blit(image, (0, 0))
    temp.set_alpha(opacity)
    bg.blit(temp, location)


class MainScreen(State.State):
    FADEINTIME = 1.0
    FADEOUTTIME = 0.2

    def __init__(self):
        self.time = 0.0
        self.color = pygame.color.Color("black")
        self.selectedColor = pygame.color.Color("black")
        Globals.SCREEN.fill(pygame.color.Color("black"))
        self.selectionID = 0
        ImageManager.unloadAll()
        ImageManager.loadSet("Astoria")
        ImageManager.loadSet("debug")
        AudioManager.loadSfxSet("menu")
        AudioManager.loadSfxSet("game")
        if AudioManager.loadedMusic != "title" or\
                not pygame.mixer.music.get_busy():
            AudioManager.loadMusic("title")
            pygame.mixer.music.play(-1)
        Globals.LASTSCREENMAIN = True
        self.astoriaToggleTime = 0.0
        self.astoriaToggleTimeInterval = 2
        self.astoriaOpacity = 0
        temp = ImageManager.levelRes["Astoria"]["Astoria1.png"]
        temp2 = ImageManager.levelRes["Astoria"]["Astoria2.png"]
        width = 500
        height = 200
        ImageManager.levelRes["Astoria"]["Astoria1.png"] =\
            pygame.transform.scale(temp, (width, height))
        ImageManager.levelRes["Astoria"]["Astoria2.png"] =\
            pygame.transform.scale(temp2, (width, height))

    def draw(self):
        temp = ImageManager.levelRes["Astoria"]["Astoria1.png"]
        temp2 = ImageManager.levelRes["Astoria"]["Astoria2.png"]
        Globals.SCREEN.blit(temp, (60, 60))
        transparentHack(
            Globals.SCREEN, temp2, (60, 60), self.astoriaOpacity)

        if self.selectionID == 0:
            temp = Globals.FONT.render("Continue", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Continue", True, self.color)
        width = 215
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (460, 250))

        if self.selectionID == 1:
            temp = Globals.FONT.render("New Game", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("New Game", True, self.color)
        width = 215
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (460, 310))

        if self.selectionID == 2:
            temp = Globals.FONT.render("High Scores", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("High Scores", True, self.color)
        width = 270
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (460, 370))

        if self.selectionID == 3:
            temp = Globals.FONT.render("Settings", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Settings", True, self.color)
        width = 215
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (460, 430))

        if self.selectionID == 4:
            temp = Globals.FONT.render("Quit", True, self.selectedColor)
        else:
            temp = Globals.FONT.render("Quit", True, self.color)
        width = 110
        height = 50
        temp = pygame.transform.scale(temp, (width, height))
        Globals.SCREEN.blit(temp, (460, 490))

    def enter_game(self):
        if Globals.GAMECOMPLETED:
            Globals.STATE = MapScreen.MapScreen()
        elif Globals.GAMESTARTED:
            pygame.mixer.music.stop()
            Globals.STATE = GameScreen.GameScreen()
            self.time = 0
        else:
            Globals.GAMESTARTED = True
            self.enter_entry()

    def enter_entry(self):
        if not Globals.PLAYER is None:
            Globals.PLAYER.kill(False)
            Globals.PLAYER = None
            World.cleanupCompletely()
        Globals.CURRENT_LEVEL = "one"
        Globals.initSunTracker(True)
        Globals.PLAYER_MAX_HEALTH = 15
        SKILL_MAX_HEALTH = 0
        PLAYER_REGEN_TIME = 7
        PLAYER_DAMAGE = 5
        SKILL_DAMAGE = 0
        PLAYER_MAX_MP = 10
        PLAYER_SKILL = 0
        PLAYER_JUMP = 610.0
        SKILL_JUMP = 0
        ARROW_VELOCITY = 700.0
        ARROW_HITS = 1
        ARROW_DAMAGE = 2
        BOW_COOLDOWN = 0.7
        MAX_SKILL = 9
        MINI_SUNS = 0
        LEVELS_BEAT = 0
        SCORE = 0
        TIME = 120
        Globals.STATE = ControlScreen.ControlScreen()

    def enter_highScore(self):
        Globals.STATE = HighScoreScreen.HighScoreScreen()

    def enter_settings(self):
        Globals.STATE = SettingScreen.SettingScreen()

    def exit_title(self):
        Globals.RUNNING = False
        pygame.mixer.music.stop()

    def update(self, time):
        if InputManager.getPressed("up"):
            self.selectionID -= 1
            if self.selectionID < 0:
                self.selectionID = 4
            AudioManager.sounds["menu"]["menuSound.ogg"].play()
        elif InputManager.getPressed("down"):
            self.selectionID = (self.selectionID + 1) % 5
            AudioManager.sounds["menu"]["menuSound.ogg"].play()

        if InputManager.getPressed("enter"):
            AudioManager.sounds["menu"]["menuSound.ogg"].play()
            AudioManager.unloadSfxSet("menu")
            if self.selectionID == 0:
                self.enter_game()
            elif self.selectionID == 1:
                self.enter_entry()
            elif self.selectionID == 2:
                self.enter_highScore()
            elif self.selectionID == 3:
                self.enter_settings()
            elif self.selectionID == 4:
                self.exit_title()
        if InputManager.getPressed("esc"):
            self.exit_title()
        self.time += time
        if self.time < MainScreen.FADEINTIME:
            ratio = self.time / MainScreen.FADEINTIME
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
