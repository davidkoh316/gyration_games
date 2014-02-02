import Component

ZORD = 0
BOW = 1


class CAttach(Component.Component):
    def __init__(self, target, flipOffset=0, equipType=ZORD):
        self.target = target
        self.flipOffset = flipOffset
        self.equipType = equipType
        target.equipType = equipType

    def initialize(self, entity):
        entity.rect = entity.image.get_rect()
        entity.hasHit = False

    def update(self, entity, interval):
        entity.posx = self.target.posx
        entity.posy = self.target.posy
        entity.state = self.target.state
        entity.sAnim = self.target.sAnim
        entity.faceRight = self.target.faceRight
        if self.equipType == ZORD:
            entity.isAttacking = self.target.isAttacking
        if not self.target.isAttacking:
            entity.hasHit = False
        entity.damage = self.target.damage
        if self.flipOffset > 0 and not entity.faceRight:
            entity.posx -= self.flipOffset
