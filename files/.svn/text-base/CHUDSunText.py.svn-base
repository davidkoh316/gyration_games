import Component
import pygame
import Globals


class CHUDSunText(Component.Component):
    def __init__(self):
        pass

    def initialize(self, entity):
        hstring = "Mini Suns: 0"
        entity.image = Globals.FONT.render(hstring, True, (255, 255, 255))
        entity.image = pygame.transform.scale(
            entity.image, (len(hstring) * 10, 50))
        entity.rect = entity.image.get_rect()
        entity.rect.x = 3.5 * Globals.WIDTH / 5.0 - entity.rect.width / 4.5
        entity.rect.y = Globals.HEIGHT - 48

    def update(self, entity, interval):
        if not Globals.PLAYER is None:
            hstring = "Mini Suns: " + str(Globals.MINI_SUNS)
            entity.image = Globals.FONT.render(hstring, True, (255, 255, 255))
            entity.image = pygame.transform.scale(
                entity.image, (len(hstring) * 10, 22))
            entity.rect = entity.image.get_rect()
            entity.rect.x = 3.5 * Globals.WIDTH / 5.0 - entity.rect.width / 4.5
            entity.rect.y = Globals.HEIGHT - 48
