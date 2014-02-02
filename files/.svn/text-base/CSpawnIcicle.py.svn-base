import CSpawner
import CAIStalactite
import math
import ImageManager
import World
import Globals
import Entity
import CPhysics
import CCollision
import CLiving
import CDamage
import CDespawn


class CSpawnIcicle(CSpawner.CSpawner):
    def update(self, entity, interval):
        distx = math.fabs(Globals.PLAYER.posx - entity.posx)
        disty = math.fabs(Globals.PLAYER.posy - entity.posy)
        if distx <= CSpawner.S_LIMIT and disty <= CSpawner.S_LIMIT and\
                not self.activated:
            self.activated = True
            s = Entity.Entity()
            s.componentList.append(CPhysics.CPhysics())
            s.componentList.append(CCollision.CCollision())
            s.componentList.append(CAIStalactite.CAIStalactite())
            s.componentList.append(CLiving.CLiving(1))
            s.componentList.append(CDamage.CDamage(5))
            s.componentList.append(CDespawn.CDespawn())
            s.image = ImageManager.levelRes["four"]["IcicleSprite.png"]
            s.initialize()
            s.rect = s.image.get_rect()
            s.rect.x = entity.rect.x
            s.rect.y = entity.rect.y
            s.posx = s.rect.x
            s.posy = s.rect.y
            World.groups["enemies"].add(s)

        elif self.activated and distx >= CSpawner.RESET_LIMIT:
            self.activated = False
