import pygame
import Component
import Globals
import ParticleFactory
import AudioManager


def hurtFunction(attackingEntity, hurtEntity, damage):
    if hurtEntity.hurtTimeout == 0.0:
        AudioManager.sounds["game"]["hitSound.ogg"].play()
        if hurtEntity == Globals.PLAYER:
            color = (255, 50, 0)
        else:
            color = (255, 255, 0)
#            print "in loop"
            Globals.SCORE = Globals.SCORE + 50
        temp = Globals.FONT.render(str(damage), True, color)
        temp = pygame.transform.scale(temp, (22 * len(str(damage)), 40))
        pos = (hurtEntity.rect.x, hurtEntity.rect.y)
        ParticleFactory.makeParticle(temp, pos, 1, (0, -2), 1)
        hurtEntity.health -= damage
        if hurtEntity.health <= 0:
            hurtEntity.health = 0
            hurtEntity.isDead = True
        hurtEntity.hurtTimeout = 1.0
        hurtEntity.stunTimeout = 0.3
        if not hurtEntity is Globals.PLAYER:
            hurtEntity.vely -= 300
            hurtEntity.isGrounded = False
            pos = attackingEntity.posx + attackingEntity.rect.width / 2.0
            if pos < hurtEntity.posx:
                hurtEntity.velx += 500
            elif pos >= hurtEntity.posx:
                hurtEntity.velx -= 500


class CLiving(Component.Component):
    def __init__(self, health=2):
        self.health = health

    def initialize(self, entity):
        entity.health = self.health
        entity.hurtFunc = hurtFunction
        entity.hurtTimeout = 0.0
        entity.stunTimeout = 0.0
        entity.isDead = False

    def update(self, entity, interval):
        entity.hurtTimeout -= interval
        entity.stunTimeout -= interval
        if entity.hurtTimeout < 0.0:
            entity.hurtTimeout = 0.0
        if entity.stunTimeout < 0.0:
            entity.stunTimeout = 0.0
        if entity.isDead:
            entity.kill()
