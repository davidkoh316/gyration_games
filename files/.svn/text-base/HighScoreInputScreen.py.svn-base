import InputManager
import State
import Globals
import pygame
import HighScoreScreen

NSIZE = (40, 50)


class HighScoreInputScreen(State.State):
    def __init__(self):
        self.sel = pygame.Surface(NSIZE)
        self.name = []
        self.ulet = 'A'
        self.color = (255, 255, 255)
        self.selColor = (180, 255, 180)
        self.msg0 = str(Globals.SCORE)
        self.msg1 = "New High Score!"
        self.msg2 = "Enter your name in 3 characters"

        self.s0 = Globals.FONT.render(self.msg0, True, self.color)
        self.s1 = Globals.FONT.render(self.msg1, True, self.color)
        self.s2 = Globals.FONT.render(self.msg2, True, self.color)

        self.s1 = pygame.transform.scale(self.s1, (400, 80))
        self.s2 = pygame.transform.scale(self.s2, (600, 70))
        Globals.GAMESTARTED = False

    def update(self, interval):
        if InputManager.getPressed("up"):
            self.ulet = chr(ord(self.ulet) - 1)
        elif InputManager.getPressed("down"):
            self.ulet = chr(ord(self.ulet) + 1)
        elif InputManager.getPressed("enter"):
            self.name.append(self.ulet)
            self.ulet = 'A'
        elif InputManager.getPressed("left"):
            self.name = self.name[:-1]
            self.ulet = 'A'

        if self.ulet < 'A':
            self.ulet = 'Z'
        elif self.ulet > 'Z':
            self.ulet = 'A'

        if len(self.name) == 3:
            f = open('highScores.txt', 'a')
            f.write(self.name[0] + self.name[1] + self.name[2] +
                    " " + str(Globals.SCORE) + "\n")
            f.close()
            Globals.SCORE = 0
            self.exit_screen()

    def draw(self):
        Globals.SCREEN.blit(
            self.s0, (Globals.WIDTH / 2.0 - self.s0.get_size()[0] / 2.0, 10))
        Globals.SCREEN.blit(
            self.s1, (Globals.WIDTH / 2.0 - self.s1.get_size()[0] / 2.0, 140))
        Globals.SCREEN.blit(
            self.s2, (Globals.WIDTH / 2.0 - self.s2.get_size()[0] / 2.0, 500))

        pos = Globals.WIDTH / 2.0 - (len(self.name) + 1) * NSIZE[0] / 2.0

        for i in range(len(self.name)):
            let = Globals.FONT.render(self.name[i], True, self.color)
            let = pygame.transform.scale(let, NSIZE)
            Globals.SCREEN.blit(
                let, (pos + i * NSIZE[0], Globals.HEIGHT / 2.0))

        let = Globals.FONT.render(self.ulet, True, self.selColor)
        let = pygame.transform.scale(let, NSIZE)
        Globals.SCREEN.blit(
            let, (pos + len(self.name) * NSIZE[0], Globals.HEIGHT / 2.0))

    def exit_screen(self):
        Globals.STATE = HighScoreScreen.HighScoreScreen()
