import Component
import pygame
import Globals


class CHUDMana(Component.Component):
    def initialize(self, entity):
        entity.image = pygame.Surface((308, 28))
        entity.rect = entity.image.get_rect()
        entity.rect.x = Globals.WIDTH / 5.0 - entity.rect.width / 2.0
        entity.rect.y = Globals.HEIGHT - 50
        self.bborder = pygame.Surface((308, 28))
        self.bborder.fill((0, 0, 0))
        self.manaBar = pygame.Surface((300, 20))

    def update(self, entity, interval):
        if Globals.PLAYER is not None:
            manaRatio =\
                float(Globals.PLAYER.mp) / float(Globals.PLAYER_MAX_MP)
        else:
            manaRatio = 0.0
        self.manaBar.fill((100, 100, 255))
        entity.image.blit(self.bborder, (0, 0))
        entity.image.blit(
            self.manaBar, (4, 4), (0, 0, int(300 * manaRatio), 20))
