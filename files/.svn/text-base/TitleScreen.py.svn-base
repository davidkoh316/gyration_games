#Title Screen
import InputManager
import ImageManager
import State
import Globals
import MainScreen
import AudioManager

import pygame.sprite
import pygame.image
import pygame.time
import pygame.mixer

import pygame.color


# main Title screen, intro animation
class TitleScreen(State.State):
    FADEINTIME = 4.0
    FADEOUTTIME = 1.0

    def __init__(self):
        self.time = 0.0
        self.color = pygame.color.Color("black")
        Globals.SCREEN.fill(pygame.color.Color("black"))
        self.temp = pygame.Surface((1, 1))
        self.text = "Gyration Games"
        self.width, self.height = Globals.FONT.size(self.text)
        self.FADEIN = True
        self.GGames = True
        self.soundPlaying = False
        AudioManager.loadSfxSet("title")
        ImageManager.loadSet("map")
        self.temp2 =\
            ImageManager.levelRes["map"]["Astoria_Map_Grass_aftersnowboss.png"]
        ImageManager.levelRes["map"]["Astoria_Map_Grass_aftersnowboss.png"] =\
            pygame.transform.scale(self.temp2, (800, 600))

    def enter_main(self):
        Globals.STATE = MainScreen.MainScreen()
        AudioManager.unloadSfxSet("title")

    def draw(self):
        if self.GGames:
            self.temp = pygame.transform.scale(self.temp, (750, 150))
            Globals.SCREEN.blit(
                self.temp,
                (Globals.WIDTH / 2 - self.temp.get_size()[0] / 2,
                    Globals.HEIGHT / 2 - self.temp.get_size()[1] / 2)
            )
        else:
            text = "Astoria_Map_Grass_aftersnowboss.png"
            self.temp2 = ImageManager.levelRes["map"][text]
            Globals.SCREEN.blit(self.temp2, (0, 0))
            self.temp = Globals.FONT.render(self.text, True, self.color)
            Globals.SCREEN.blit(
                self.temp,
                (Globals.WIDTH / 2 - self.width / 2,
                    Globals.HEIGHT / 2 - self.height / 2)
            )

    def update(self, time):
        if InputManager.getAction("jump") or InputManager.getAction("enter"):
            self.enter_main()
        self.time += time
        if self.time < TitleScreen.FADEINTIME and self.FADEIN:
            if not self.GGames and not self.soundPlaying:
                self.text = "Astoria"
                AudioManager.sounds["title"]["staticRustle.ogg"].play()
                self.soundPlaying = True
            ratio = self.time / TitleScreen.FADEINTIME
            value = int(ratio * 255)
            self.color = pygame.color.Color(value, value, value)
        elif self.time < TitleScreen.FADEOUTTIME and not self.FADEIN:
            ratio = 1.0 - self.time / TitleScreen.FADEOUTTIME
            value = int(ratio * 255)
            self.color = pygame.color.Color(value, value, value)
        else:
            self.time = 0
            if not self.FADEIN:
                if self.GGames:
                    self.GGames = False
                    TitleScreen.FADEINTIME = 4.0
                else:
                    self.enter_main()
            self.FADEIN = not self.FADEIN
        self.width, self.height = Globals.FONT.size(self.text)
        self.temp = Globals.FONT.render(self.text, True, self.color)
