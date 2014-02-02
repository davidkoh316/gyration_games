import Component


class CProjectile(Component.Component):
    def __init__(self, img, pos, vel, acc=(0, 0), lifeHit=1, lifeTime=2):
        self.img = img
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.lifeHit = lifeHit
        self.lifeTime = lifeTime
        self.time = 0.0

    def initialize(self, entity):
        entity.isFlying = True
        entity.hasHit = False
        entity.posx = self.pos[0]
        entity.posy = self.pos[1]
        entity.velx = self.vel[0]
        entity.vely = self.vel[1]
        entity.accx = self.acc[0]
        entity.accy = self.acc[1]
        entity.image = self.img
        entity.rect = entity.image.get_rect()
        entity.rect.x = int(self.pos[0])
        entity.rect.y = int(self.pos[1])

    def update(self, entity, interval):
        if entity.hasHit:
            entity.hasHit = False
            self.lifeHit -= 1
            if self.lifeHit == 0:
                entity.kill()
        elif entity.velx == 0.0:
            entity.kill()
        self.time += interval
        if self.lifeTime < self.time:
            entity.kill()
