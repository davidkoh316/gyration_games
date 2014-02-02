import Component
import pygame
import Globals


class CHUDBoss(Component.Component):
    def initialize(self, entity):
        entity.image = pygame.Surface((550, 30))
        entity.rect = entity.image.get_rect()
        entity.rect.x = Globals.WIDTH / 2.0 - entity.rect.width / 2.0
        entity.rect.y = 32
        self.bborder = pygame.Surface((550, 30))
        self.bborder.fill((50, 40, 70))
        self.healthBar = pygame.Surface((544, 24))
        self.healthBar.fill((255, 0, 0))

    def update(self, entity, interval):
        if Globals.BOSS is not None:
            healthRatio = float(Globals.BOSS.health) / 500.0
        else:
            healthRatio = 0.0
        entity.image.blit(self.bborder, (0, 0))
        entity.image.blit(
            self.healthBar,
            (3, 3),
            (0, 0, int(544 * healthRatio), 24))
