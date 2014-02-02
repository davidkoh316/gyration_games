import Component
import CPhysics
import random
import math
import Globals

MOVEMENT_SPEED = 200.0
DIVING_SPEED = 50.0
TIME_PER_DIR_CHANGE = 1


class CAIBirdDiving(Component.Component):
    def initialize(self, entity):
        hasPhysics = False
        for component in entity.componentList:
            if isinstance(component, CPhysics.CPhysics):
                hasPhysics = True
        if not hasPhysics:
            raise Exception("CAIFlying requires CPhysics")
        entity.dirChangeTime = 0
        entity.velx = random.uniform(-MOVEMENT_SPEED, MOVEMENT_SPEED)
        entity.vely = 0
        entity.accy = 0
        entity.isFlying = True
        entity.faceRight = True
        self.state = 0

    def update(self, entity, interval):
        entity.dirChangeTime += interval
        if entity.velx < 0:
            entity.faceRight = False
        else:
            entity.faceRight = True
        if abs(entity.rect.x - Globals.PLAYER.rect.x) < 3 and\
                (Globals.PLAYER.rect.y - entity.rect.y) < 400 and\
                self.state == 0:
            dive = random.randint(0, 2)
            if dive < 1:
                self.state = 1
                entity.state = 1
        if self.state == 1:
            if entity.rect.y < Globals.PLAYER.rect.y:
                entity.vely = entity.vely + DIVING_SPEED
            else:
                self.state = 2
                entity.state = 0
                entity.vely = -entity.vely
        if self.state == 2:
            if entity.vely < 0:
                entity.vely = entity.vely + DIVING_SPEED
            else:
                entity.vely = 0
                self.state = 0
        if self.state == 0:
            if entity.vely != 0:
                entity.vely /= 2.0
        if entity.dirChangeTime >= TIME_PER_DIR_CHANGE:
            entity.velx = random.uniform(-MOVEMENT_SPEED, MOVEMENT_SPEED)
            #entity.vely = 0
            entity.dirChangeTime = 0
            if entity.vely < 0:
                entity.isGrounded = False
