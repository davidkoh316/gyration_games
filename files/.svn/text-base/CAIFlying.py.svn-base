import Component
import CPhysics
import random

MOVEMENT_SPEED = 200.0
TIME_PER_DIR_CHANGE = 1


class CAIFlying(Component.Component):
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

    def update(self, entity, interval):
        entity.dirChangeTime += interval
        if entity.velx < 0:
            entity.faceRight = False
        else:
            entity.faceRight = True
        if entity.dirChangeTime >= TIME_PER_DIR_CHANGE:
            entity.velx = random.uniform(-MOVEMENT_SPEED, MOVEMENT_SPEED)
            entity.vely = 0
            entity.dirChangeTime = 0
            if entity.vely < 0:
                entity.isGrounded = False
