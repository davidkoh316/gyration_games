import Component
import pygame
import Globals


class CHUDScoreText(Component.Component):
    def __init__(self):
        pass

    def initialize(self, entity):
        hstring = "Score: 0"
        entity.image = Globals.FONT.render(hstring, True, (255, 255, 255))
        entity.image = pygame.transform.scale(
            entity.image, (len(hstring) * 10, 50))
        entity.rect = entity.image.get_rect()
        entity.rect.x = 3.5 * Globals.WIDTH / 5.0 - entity.rect.width / 5.0
        entity.rect.y = Globals.HEIGHT - 78

    def update(self, entity, interval):
        if not Globals.PLAYER is None:
            hstring = "Score: " + str(Globals.SCORE)
            entity.image = Globals.FONT.render(hstring, True, (255, 255, 255))
            entity.image = pygame.transform.scale(
                entity.image, (len(hstring) * 10, 22))
            entity.rect = entity.image.get_rect()
            entity.rect.x = 4.0 * Globals.WIDTH / 5.0 - entity.rect.width / 2.0
            entity.rect.y = Globals.HEIGHT - 78
