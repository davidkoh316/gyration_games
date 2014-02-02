import pygame
import Component

SECONDS_PER_ANIMATION = 0.3


def updatePosition(entity):
    v = vars(entity)
    if 'posx' in v and 'posy' in v:
        entity.rect.x = int(entity.posx)
        entity.rect.y = int(entity.posy)


class Entity(pygame.sprite.Sprite):
    """Entity is a base class for things in the game world."""
    def __init__(self):
        super(Entity, self).__init__()
        self.componentList = []
        self.initialized = False
        self.update_pos = updatePosition
        self.kFunc = []
        self.drawFunc = []

    def initialize(self):
        if not self.initialized:
            for component in self.componentList:
                if not isinstance(component, Component.Component):
                    raise Exception(
                        "Classes in componentList must be a component")
                component.initialize(self)
            self.initialized = True

    def update(self, interval):
        for component in self.componentList:
            component.update(self, interval)
        self.update_pos(self)

    def kill(self, useKillFunc=True):
        if useKillFunc:
            for func in self.kFunc:
                func(self)
        super(Entity, self).kill()
