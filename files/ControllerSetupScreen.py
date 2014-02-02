import InputManager
import State
import SettingScreen
import Globals
import pygame


class ControllerSetupScreen(State.State):
    def __init__(self):
        self.selectionID = 0
        self.color = pygame.color.Color("white")
        self.selectedColor = pygame.color.Color(127, 255, 127)
        Globals.SCREEN.fill(pygame.color.Color("black"))
        self.cExists = InputManager.initController()
        self.index = 0
        self.iText = "default"
        self.wait = 0.0

    def update(self, interval):
        if InputManager.getPressed("esc"):
            Globals.STATE = SettingScreen.SettingScreen()
        if self.cExists:
            if self.index < len(InputManager.cList):
                self.iText = "Press button/axis for " +\
                    InputManager.cList[self.index]

            if self.wait == 0.0 and self.index < len(InputManager.cList):
                cInput = InputManager.getControllerInput()
                if cInput[0] != 0:
                    InputManager.cBindings[cInput] =\
                        InputManager.cList[self.index]
                    self.index += 1
                    self.wait = 1.0
            elif self.wait == 0.0:
                InputManager.cConfigured = True
                Globals.STATE = SettingScreen.SettingScreen()
            else:
                self.wait -= interval
                if self.wait < 0.0:
                    self.wait = 0.0

    def draw(self):
        info = Globals.FONT.render(
            "Controller Setup", True, self.selectedColor)
        info = pygame.transform.scale(info, (600, 120))
        Globals.SCREEN.blit(info, (100, 40))

        info = Globals.FONT.render("(Esc to cancel)", True, self.color)
        info = pygame.transform.scale(info, (470, 50))
        Globals.SCREEN.blit(info, (165, 180))

        if self.wait > 0.0:
            color = self.color
        else:
            color = self.selectedColor
        info = Globals.FONT.render(self.iText, True, color)
        info = pygame.transform.scale(info, (600, 90))
        Globals.SCREEN.blit(info, (100, 300))
