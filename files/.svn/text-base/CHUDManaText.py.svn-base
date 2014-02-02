import Component
import pygame
import Globals


class CHUDManaText(Component.Component):
    def __init__(self):
        pass

    def initialize(self, entity):
        mstring = "0 / 0"
        entity.image = Globals.FONT.render(mstring, True, (255, 255, 255))
        entity.image = pygame.transform.scale(
            entity.image, (len(mstring) * 10, 22))
        entity.rect = entity.image.get_rect()
        entity.rect.x = Globals.WIDTH / 5.0 - entity.rect.width / 2.0
        entity.rect.y = Globals.HEIGHT - 48

    def update(self, entity, interval):
        if not Globals.PLAYER is None:
            mstring = str(Globals.PLAYER.mp) + " / " +\
                str(Globals.PLAYER_MAX_MP)
            entity.image = Globals.FONT.render(mstring, True, (255, 255, 255))
            entity.image = pygame.transform.scale(
                entity.image, (len(mstring) * 10, 22))
            entity.rect = entity.image.get_rect()
            entity.rect.x = Globals.WIDTH / 5.0 - entity.rect.width / 2.0
            entity.rect.y = Globals.HEIGHT - 48
