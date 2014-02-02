import Component

gravity = 1200


class CPhysics(Component.Component):
    def initialize(self, entity):
        entity.accx = 0
        entity.accy = gravity
        entity.velx = 0
        entity.vely = 0
        entity.posx = 0
        entity.posy = 0
        entity.isGrounded = False

    def update(self, entity, interval):
        entity.velx = entity.velx + entity.accx * interval
        entity.vely = entity.vely + entity.accy * interval
        entity.posx = entity.posx + entity.velx * interval
        entity.posy = entity.posy + entity.vely * interval
        v = vars(entity)
        if "isFlying" not in v:
            if not entity.isGrounded:
                entity.accy = gravity
            else:
                entity.accy = 0
