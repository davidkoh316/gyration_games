import Component
import pygame

## Style flags
# 0 - nothing
FLY_UPWARDS = 1     # - fly upwards
FLY_DOWNWARDS = 1 << 1
SIDE_SIDE = 1 << 2  # - side-to-side floaty movement
SPIN_CLOCKWISE = 1 << 3  # rotation of particle
SPIN_CCLOCKWISE = 1 << 4
EXPLODE = 1 << 5


def pdraw(entity, screen):
    screen.blit(
        entity.image, (entity.rect.x, entity.rect.y), None, entity.pdFlags)


class CParticle(Component.Component):
    def __init__(
            self, sprite, pos, lifetime=1, direction=(0, 0), style=0, flags=0):
        self.sprite = sprite
        self.pos = pos
        self.lifetime = lifetime
        self.currentTime = 0.0
        self.direction = direction
        self.style = style
        self.flags = flags
        self.angle = 0.0

    def initialize(self, entity):
        entity.image = self.sprite
        entity.rect = entity.image.get_rect()
        entity.posx = self.pos[0]
        entity.posy = self.pos[1]
        entity.pdFlags = self.flags
        entity.pdraw = pdraw

    def update(self, entity, interval):
        if self.style & FLY_UPWARDS > 0:
            self.direction = (self.direction[0], self.direction[1] - 1)
        if self.style & FLY_DOWNWARDS > 0:
            self.direction = (self.direction[0], self.direction[1] + 1)
        if self.style & SIDE_SIDE > 0:
            pass
        if self.style & SPIN_CLOCKWISE > 0:
            self.angle -= 20.0
            entity.image = pygame.transform.rotate(self.sprite, self.angle)
        if self.style & SPIN_CCLOCKWISE > 0:
            self.angle += 20.0
            entity.image = pygame.transform.rotate(self.sprite, self.angle)
        if self.style & EXPLODE > 0:
            self.direction = (self.direction[0] * 1.2, self.direction[1] * 1.2)

        entity.posx += self.direction[0]
        entity.posy += self.direction[1]

        self.currentTime += interval
        if self.currentTime > self.lifetime:
            entity.kill()
        else:
            ratio = 1.0 - self.currentTime / self.lifetime
            entity.image.set_alpha(int(255 * ratio))
