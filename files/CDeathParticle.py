import Component
import ParticleFactory


def kfunc(entity):
    ParticleFactory.makeParticle(
        entity.deathImage,
        (entity.rect.x, entity.rect.y),
        entity.deathLifetime,
        entity.deathDirection,
        entity.deathStyle,
        entity.deathFlags)


class CDeathParticle(Component.Component):
    def __init__(self, image, lifetime=1, direction=(0, 0), style=0, flags=0):
        self.image = image
        self.lifetime = lifetime
        self.direction = direction
        self.style = style
        self.flags = flags

    def initialize(self, entity):
        entity.deathImage = self.image
        entity.deathLifetime = self.lifetime
        entity.deathDirection = self.direction
        entity.deathStyle = self.style
        entity.deathFlags = self.flags
        entity.kFunc.append(kfunc)
