import Component
import View
import pygame
import ImageManager

rate = [
    0.1,
    0.3,
    0.5,
    0.8
]


class CBackground(Component.Component):
    def __init__(self, level):
        ImageManager.loadSet(level)
        if "Layer0.png" in ImageManager.levelRes[level]:
            self.bg0 = ImageManager.levelRes[level]["Layer0.png"]
        if "Layer1.png" in ImageManager.levelRes[level]:
            self.bg1 = ImageManager.levelRes[level]["Layer1.png"]
        if "Layer2.png" in ImageManager.levelRes[level]:
            self.bg2 = ImageManager.levelRes[level]["Layer2.png"]
        if "Layer3.png" in ImageManager.levelRes[level]:
            self.bg3 = ImageManager.levelRes[level]["Layer3.png"]

    def initialize(self, entity):
        entity.image = pygame.Surface((800, 600))
        entity.rect = entity.image.get_rect()

    def update(self, entity, interval):
        v = vars(self)
        if "bg0" in v:
            x = (rate[0] * View.viewx) % self.bg0.get_size()[0]
            entity.image.blit(self.bg0, (-x, 0))
            entity.image.blit(self.bg0, (-(x) + self.bg0.get_size()[0], 0))
        if "bg1" in v:
            x = (rate[1] * View.viewx) % self.bg1.get_size()[0]
            entity.image.blit(self.bg1, (-x, 0))
            entity.image.blit(self.bg1, (-(x) + self.bg1.get_size()[0], 0))
        if "bg2" in v:
            x = (rate[2] * View.viewx) % self.bg2.get_size()[0]
            entity.image.blit(self.bg2, (-x, 0))
            entity.image.blit(self.bg2, (-(x) + self.bg2.get_size()[0], 0))
        if "bg3" in v:
            x = (rate[3] * View.viewx) % self.bg3.get_size()[0]
            entity.image.blit(self.bg3, (-x, 0))
            entity.image.blit(self.bg3, (-(x) + self.bg3.get_size()[0], 0))
