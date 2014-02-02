import Component
import CPhysics
import random

MOVEMENT_SPEED = 200.0
TIME_PER_DIR_CHANGE = 1


class CAIRandom(Component.Component):
    def initialize(self, entity):
        hasPhysics = False
        for component in entity.componentList:
            if isinstance(component, CPhysics.CPhysics):
                hasPhysics = True
        if not hasPhysics:
            raise Exception("CAIRandom requires CPhysics")
        entity.dirChangeTime = 0
        entity.velx = random.uniform(-MOVEMENT_SPEED, MOVEMENT_SPEED)
        entity.vely = random.uniform(-MOVEMENT_SPEED, 0)

    def update(self, entity, interval):
        entity.dirChangeTime += interval
        if entity.dirChangeTime >= TIME_PER_DIR_CHANGE:
            entity.velx = random.uniform(-MOVEMENT_SPEED, MOVEMENT_SPEED)
            entity.vely = random.uniform(-MOVEMENT_SPEED * 2, 0)
            entity.dirChangeTime = 0
            if entity.vely < 0:
                entity.isGrounded = False
            if entity.velx > 0:
                entity.faceRight = True
            else:
                entity.faceRight = False
