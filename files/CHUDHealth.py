import Component
import pygame
import Globals


class CHUDHealth(Component.Component):
    def initialize(self, entity):
        entity.image = pygame.Surface((308, 28))
        entity.rect = entity.image.get_rect()
        entity.rect.x = Globals.WIDTH / 5.0 - entity.rect.width / 2.0
        entity.rect.y = Globals.HEIGHT - 50
        self.bborder = pygame.Surface((308, 28))
        self.bborder.fill((0, 0, 0))
        self.healthBar = pygame.Surface((300, 20))

    def update(self, entity, interval):
        if Globals.PLAYER is not None:
            healthRatio =\
                float(Globals.PLAYER.health) / float(Globals.PLAYER_MAX_HEALTH)
        else:
            healthRatio = 0.0
        self.healthBar.fill(((1.0 - healthRatio) * 255, healthRatio * 255, 0))
        entity.image.blit(self.bborder, (0, 0))
        entity.image.blit(
            self.healthBar, (4, 4), (0, 0, int(300 * healthRatio), 20))
