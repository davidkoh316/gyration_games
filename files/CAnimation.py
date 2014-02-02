import pygame
import Component
import ParticleFactory


# animStyle:
# 0 - 1,2,3,1,2,3   repeat
# 1 - 1,2,3,2,1,2,3 cycle

class CAnimation(Component.Component):
    def __init__(self, spriteSheet, numOfAnims=3, numOfStates=6, animStyle=1,
                 secondsPerAnimation=0.3):
        self.spriteSheet = spriteSheet
        self.numOfAnims = numOfAnims
        self.numOfStates = numOfStates
        self.animStyle = animStyle
        self.secondsPerAnimation = secondsPerAnimation

    def initialize(self, entity):
        entity.state = 0
        entity.sAnim = 0
        entity.sAnimTick = 0
        entity.aForward = True
        size = self.spriteSheet.get_size()
        entity.size = (size[0] / self.numOfAnims, size[1] / self.numOfStates)
        entity.image = pygame.Surface(entity.size)
        entity.rect = pygame.Rect(0, 0, entity.size[0], entity.size[1])
        entity.faceRight = True
        entity.isAttacking = False

    def update(self, entity, interval):
        entity.sAnimTick += interval
        if self.secondsPerAnimation != 0 and\
            entity.sAnimTick >= self.secondsPerAnimation and\
                not entity.isAttacking:
            entity.sAnimTick -= self.secondsPerAnimation
            if self.animStyle == 0:
                entity.sAnim += 1
                if entity.sAnim >= self.numOfAnims:
                    entity.sAnim = 0
            elif self.animStyle == 1:
                if entity.aForward:
                    entity.sAnim += 1
                    if entity.sAnim >= self.numOfAnims:
                        entity.sAnim = 1
                        entity.aForward = False
                else:
                    entity.sAnim -= 1
                    if entity.sAnim < 0:
                        entity.sAnim = 1
                        entity.aForward = True
        elif self.secondsPerAnimation != 0 and\
                entity.isAttacking:
            if (
                'attackLength' in vars(entity) and
                entity.sAnimTick >= entity.attackLength) or (
                    not 'attackLength' in vars(entity) and
                    entity.sAnimTick >= self.secondsPerAnimation):
                entity.sAnim += 1
                if entity.sAnim > entity.asAnimEnd:
                    entity.isAttacking = False
                    entity.state = 0
                    entity.sAnim = 0
                if 'asAnimParticle' in vars(entity) and\
                    'attackParticle' in vars(entity) and\
                        entity.sAnim == entity.asAnimParticle:
                    rev = 1.0
                    if not entity.faceRight:
                        rev = -1.0
                    ParticleFactory.makeParticle(
                        entity.attackParticle,
                        (entity.posx + rev * 30, entity.posy + 40),
                        1,
                        (rev * 7, 0),
                        1)
        entity.image = self.spriteSheet.subsurface(
            (entity.size[0] * entity.sAnim, entity.size[1] * entity.state,
                entity.size[0], entity.size[1]))
        if not entity.faceRight:
            entity.image = pygame.transform.flip(entity.image, 1, 0)
