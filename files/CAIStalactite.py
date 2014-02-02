import Component
import CPhysics
import Globals


class CAIStalactite(Component.Component):
    def initialize(self, entity):
        entity.accy = 0
        self.falling = False
        entity.isGrounded = False
        entity.isFlying = True

    def update(self, entity, interval):
        if not self.falling:
            dist = Globals.PLAYER.posx + Globals.PLAYER.rect.width / 2.0\
                - entity.posx - entity.rect.width / 2.0
            if dist*dist < 1600:
                entity.accy = CPhysics.gravity
                self.falling = True
        if self.falling and entity.isGrounded:
            entity.kill()
