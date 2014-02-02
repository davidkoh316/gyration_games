import ImageManager
import World
import Component
import Globals
import random
import math
import Entity
import CPhysics
import CCollision
import CLiving
import CDamage
import CTimedDespawn
import pygame
import ParticleFactory
import CParticle
import CAnimation
import CAIRandom
import CParticle
import CDeathParticle


FACE_RIGHT = False
IS_THROWING = False
ARM_PHASE = 0
ARMS_OFFSET = (-37, -23)
ARMS_OFFSET_L = (-57, -23)


def kFunc(entity):
    entity.topPart.kill()
    entity.midPart.kill()
    Globals.WIN = True
    Globals.BOSS = None
    ParticleFactory.makeParticle(
        ImageManager.levelRes["boss"]["snowmanDead.png"],
        (entity.rect.x, entity.rect.y),
        3.0,
        (0, -30),
        CParticle.FLY_DOWNWARDS | CParticle.SPIN_CLOCKWISE,
        pygame.BLEND_ADD)
    Globals.GAMECOMPLETED = True


def drawNormal(entity, screen):
    global FACE_RIGHT
    if FACE_RIGHT:
        screen.blit(
            entity.image, (entity.rect.x, entity.rect.y))
    else:
        screen.blit(
            pygame.transform.flip(entity.image, True, False),
            (entity.rect.x, entity.rect.y))


def drawArms(entity, screen):
    global FACE_RIGHT
    global IS_THROWING
    global ARM_PHASE
    global ARMS_OFFSET
    global ARMS_OFFSET_L
    if IS_THROWING:
        if FACE_RIGHT:
            screen.blit(entity.image, (entity.rect.x, entity.rect.y))
            screen.blit(
                ImageManager.levelRes["boss"]["snowmanArmsThrowing.png"],
                (entity.rect.x + ARMS_OFFSET[0],
                    entity.rect.y + ARMS_OFFSET[1]),
                pygame.Rect(214 * ARM_PHASE, 0, 214, 91))
        else:
            screen.blit(
                pygame.transform.flip(entity.image, True, False),
                (entity.rect.x, entity.rect.y))
            screen.blit(
                pygame.transform.flip(
                    ImageManager.levelRes["boss"]["snowmanArmsThrowing.png"],
                    True,
                    False),
                (entity.rect.x + ARMS_OFFSET_L[0],
                    entity.rect.y + ARMS_OFFSET_L[1]),
                pygame.Rect(214 * (2 - ARM_PHASE), 0, 214, 91))
    else:
        if FACE_RIGHT:
            screen.blit(entity.image, (entity.rect.x, entity.rect.y))
            screen.blit(
                ImageManager.levelRes["boss"]["snowmanArmsStanding.png"],
                (entity.rect.x + ARMS_OFFSET[0],
                    entity.rect.y + ARMS_OFFSET[1]),
                pygame.Rect(214 * ARM_PHASE, 0, 214, 91))
        else:
            screen.blit(
                pygame.transform.flip(entity.image, True, False),
                (entity.rect.x, entity.rect.y))
            screen.blit(
                pygame.transform.flip(
                    ImageManager.levelRes["boss"]["snowmanArmsStanding.png"],
                    True,
                    False),
                (entity.rect.x + ARMS_OFFSET_L[0],
                    entity.rect.y + ARMS_OFFSET_L[1]),
                pygame.Rect(214 * ARM_PHASE, 0, 214, 91))


def spawnIcicle():
    s = Entity.Entity()
    s.componentList.append(CPhysics.CPhysics())
    s.componentList.append(CCollision.CCollision())
    s.componentList.append(CLiving.CLiving(1))
    s.componentList.append(CDamage.CDamage(2))
    s.componentList.append(CTimedDespawn.CTimedDespawn(1.5))
    s.image = ImageManager.levelRes["five"]["IcicleSprite.png"]
    s.initialize()
    s.rect = s.image.get_rect()
    return s


def spawnIcicles(midPart):
    for i in range(random.randint(3, 7)):
        s = spawnIcicle()
        s.rect.x = midPart.rect.x
        s.rect.y = midPart.rect.y
        s.posx = s.rect.x
        s.posy = s.rect.y
        s.velx = (random.random() - 0.5) * 600
        s.vely = -800
        World.groups["enemies"].add(s)


def spawnMinion():
    m = Entity.Entity()
    m.componentList.append(CAnimation.CAnimation(
        ImageManager.levelRes["boss"]["Snowbally.png"], 2, 1, 0))
    m.componentList.append(CPhysics.CPhysics())
    m.componentList.append(CAIRandom.CAIRandom())
    m.componentList.append(CCollision.CCollision())
    m.componentList.append(CLiving.CLiving(16))
    m.componentList.append(CDamage.CDamage(2))
    m.componentList.append(CTimedDespawn.CTimedDespawn(12))
    m.componentList.append(CDeathParticle.CDeathParticle(
        ImageManager.levelRes["boss"]["snowballDead.png"],
        3,
        (0, -20),
        CParticle.FLY_DOWNWARDS,
        pygame.BLEND_ADD))
    m.initialize()
    return m


def spawnMinions(botPart):
    for i in range(random.randint(1, 3)):
        m = spawnMinion()
        m.rect.x = botPart.rect.x + 10
        m.rect.y = botPart.rect.y
        m.posx = m.rect.x
        m.posy = m.rect.y
        m.velx = (random.random() - 0.5) * 600
        m.vely = -500
        World.groups["enemies"].add(m)


class CSnowbossBot(Component.Component):
    def __init__(self, topPart, midPart):
        self.topPart = topPart
        self.midPart = midPart
        topPart.isFlying = True
        midPart.isFlying = True

    def initialize(self, entity):
        entity.topPart = self.topPart
        entity.midPart = self.midPart
        entity.kFunc.append(kFunc)
        self.topPart.accy = 0
        self.midPart.accy = 0
        self.phase = 0
        self.mphase = -1
        self.faceRight = True
        self.pDir = (0, 0)
        self.dPos = 0
        self.topPart.draw = drawNormal
        self.midPart.draw = drawArms
        entity.draw = drawNormal
        self.aPTimer = 0.0

    def update(self, entity, interval):
        global FACE_RIGHT
        global IS_THROWING
        global ARM_PHASE
        if Globals.PLAYER.posx < entity.posx:
            FACE_RIGHT = False
        else:
            FACE_RIGHT = True

        if not IS_THROWING:
            self.aPTimer += interval
            if self.aPTimer > 0.8:
                self.aPTimer = 0.0
                ARM_PHASE = (ARM_PHASE + 1) % 2

        if self.dPos == 0:  # move to default position
            x = entity.rect.x + 20
            vx = self.midPart.rect.x

            self.midPart.velx = (x - vx) * 3.0

            y = entity.rect.y - 85
            vy = self.midPart.rect.y

            self.midPart.vely = (y - vy) * 3.0

            x = self.midPart.rect.x + 20
            vx = self.topPart.rect.x

            self.topPart.velx = (x - vx) * 3.0

            y = self.midPart.rect.y - 65
            vy = self.topPart.rect.y

            self.topPart.vely = (y - vy) * 3.0
        elif self.dPos == 1:  # move to default mid part only
            x = entity.rect.x + 20
            vx = self.midPart.rect.x

            self.midPart.velx = (x - vx) * 3.0

            y = entity.rect.y - 85
            vy = self.midPart.rect.y

            self.midPart.vely = (y - vy) * 3.0

        if self.phase == 1:  # "aim" at player
            self.pDir = (Globals.PLAYER.posx - self.topPart.posx,
                         Globals.PLAYER.posy - self.topPart.posy)
            dirLen = math.sqrt(
                self.pDir[0] * self.pDir[0] + self.pDir[1] * self.pDir[1])
            self.pDir = (self.pDir[0]/dirLen, self.pDir[1]/dirLen)
        elif self.phase == 2:  # "throw at player
            self.topPart.velx = 500 * self.pDir[0] * (1.3 - self.mtime)
            self.topPart.vely = 500 * self.pDir[1] * (1.3 - self.mtime)

        if self.mphase == -1:  # randomly pick next move
            self.phase = 0
            r = random.random()
            if r < 0.2:  # pick jump
                self.mphase = 0
                self.mtimer = 2.0
                self.mtime = 0.0
                entity.isGrounded = False
                entity.vely = -700
                if Globals.PLAYER.rect.x < entity.rect.x:
                    entity.velx = -400
                    self.faceRight = False
                else:
                    entity.velx = 400
                    self.faceRight = True
            elif r < 0.4:  # pick throw
                self.mphase = 1
                self.mtimer = 1.0
                self.mtime = 0.0
                self.phase = 1
                IS_THROWING = True
                ARM_PHASE = 0
            elif r < 0.6:  # pick spawn
                self.mphase = 4
                self.mtimer = 2.2
                self.mtime = 0.0
                spawnMinions(entity)
            elif r < 0.8:  # throw icicles
                self.mphase = 5
                self.mtimer = 2.0
                self.mtime = 0.0
                spawnIcicles(self.midPart)
            else:
                self.mphase = -1
        elif self.mphase == 0:  # jump at player
            if entity.isGrounded is True:
                self.mtime += interval
                if self.mtime > self.mtimer:
                    self.mphase = -1
                    entity.accx = 0.0
            elif entity.velx == 0.0:
                if self.faceRight:
                    entity.velx = 400
                else:
                    entity.velx = -400
        elif self.mphase == 1:  # throw phase 1 - pause
            self.mtime += interval
            if self.mtime > self.mtimer:
                self.mphase = 2
                self.mtime = 0.0
                self.mtimer = 1.3
                ARM_PHASE = 1
        elif self.mphase == 2:  # throw phase 2 - throw
            self.mtime += interval
            self.dPos = 1
            self.phase = 2
            if self.mtime > 0.3:
                ARM_PHASE = 2
            if self.mtime > self.mtimer:
                self.mphase = 3
                self.mtime = 0.0
                self.mtimer = 0.5
                ARM_PHASE = 1

        elif self.mphase == 3:  # throw phase 3 - return
            self.mtime += interval
            self.dPos = 0
            self.phase = 0
            if self.mtime > 0.2:
                ARM_PHASE = 0
            if self.mtime > self.mtimer:
                self.mphase = -1
                IS_THROWING = False
        elif self.mphase == 4:  # spawn minions
            self.mtime += interval
            if self.mtime > self.mtimer:
                self.mphase = -1
        elif self.mphase == 5:
            self.mtime += interval
            if self.mtime > self.mtimer:
                self.mphase = -1

        if entity.isGrounded is True:
            entity.accx = -entity.velx * 3.0
