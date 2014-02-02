import Component
import pygame
import Globals


class CHUDHealthText(Component.Component):
    def __init__(self):
        pass

    def initialize(self, entity):
        hstring = "0 / 0"
        entity.image = Globals.FONT.render(hstring, True, (255, 255, 255))
        entity.image = pygame.transform.scale(
            entity.image, (len(hstring) * 10, 22))
        entity.rect = entity.image.get_rect()
        entity.rect.x = Globals.WIDTH / 5.0 - entity.rect.width / 2.0
        entity.rect.y = Globals.HEIGHT - 48

    def update(self, entity, interval):
        if not Globals.PLAYER is None:
            hstring = str(Globals.PLAYER.health) + " / " +\
                str(Globals.PLAYER_MAX_HEALTH)
            entity.image = Globals.FONT.render(hstring, True, (255, 255, 255))
            entity.image = pygame.transform.scale(
                entity.image, (len(hstring) * 10, 22))
            entity.rect = entity.image.get_rect()
            entity.rect.x = Globals.WIDTH / 5.0 - entity.rect.width / 2.0
            entity.rect.y = Globals.HEIGHT - 78
