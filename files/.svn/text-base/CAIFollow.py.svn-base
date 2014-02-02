import Component
import CPhysics
import random
import Globals

MOVEMENT_SPEED = 200.0
TIME_PER_DIR_CHANGE = 1


class CAIFollow(Component.Component):
    def initialize(self, entity):
        hasPhysics = False
        for component in entity.componentList:
            if isinstance(component, CPhysics.CPhysics):
                hasPhysics = True
        if not hasPhysics:
            raise Exception("CAIFollow requires CPhysics")
        entity.dirChangeTime = 0
        entity.velx = random.uniform(-MOVEMENT_SPEED, MOVEMENT_SPEED)
        entity.vely = random.uniform(-MOVEMENT_SPEED, 0)

    def update(self, entity, interval):
        if entity.rect.x < Globals.PLAYER.rect.x:
            entity.velx = random.uniform(0, MOVEMENT_SPEED)
        else:
            entity.velx = random.uniform(-MOVEMENT_SPEED, 0)
        entity.dirChangeTime += interval
        if entity.dirChangeTime >= TIME_PER_DIR_CHANGE:
            #entity.velx = random.uniform(-MOVEMENT_SPEED, MOVEMENT_SPEED)
            entity.vely = random.uniform(-MOVEMENT_SPEED * 2, 0)
            entity.dirChangeTime = 0
            if entity.vely < 0:
                entity.isGrounded = False
