import CSpawner
import Entity
import CSnowbossBot
import World
import CPhysics
import CDamage
import CCollision
import CLiving
import ImageManager
import Globals


class CSpawnSnowboss(CSpawner.CSpawner):
    def __init__(self):
        super(CSpawnSnowboss, self).__init__(1)
        self.spawned = False

    def update(self, entity, interval):
        if not self.spawned:
            self.spawned = True
            snowbossTop = Entity.Entity()
            snowbossMid = Entity.Entity()
            snowbossBot = Entity.Entity()

            snowbossTop.componentList.append(CPhysics.CPhysics())
            snowbossTop.componentList.append(CDamage.CDamage(3))

            snowbossMid.componentList.append(CPhysics.CPhysics())
            snowbossMid.componentList.append(CDamage.CDamage(4))

            snowbossBot.componentList.append(CPhysics.CPhysics())
            snowbossBot.componentList.append(CCollision.CCollision())
            snowbossBot.componentList.append(CDamage.CDamage(6))
            snowbossBot.componentList.append(CLiving.CLiving(500))
            snowbossBot.componentList.append(
                CSnowbossBot.CSnowbossBot(snowbossTop, snowbossMid))

            World.groups["boss"].add(snowbossTop)
            World.groups["boss"].add(snowbossMid)
            World.groups["boss"].add(snowbossBot)
            snowbossTop.initialize()
            snowbossMid.initialize()
            snowbossBot.initialize()
            snowbossTop.posx = entity.posx
            snowbossTop.posy = entity.posy
            snowbossMid.posx = entity.posx
            snowbossMid.posy = entity.posy
            snowbossBot.posx = entity.posx
            snowbossBot.posy = entity.posy

            snowbossTop.image = ImageManager.levelRes["boss"]["snowmanTop.png"]
            snowbossTop.rect = snowbossTop.image.get_rect()
            snowbossMid.image = ImageManager.levelRes["boss"]["snowmanMid.png"]
            snowbossMid.rect = snowbossMid.image.get_rect()
            snowbossBot.image = ImageManager.levelRes["boss"]["snowmanBot.png"]
            snowbossBot.rect = snowbossBot.image.get_rect()

            Globals.BOSS = snowbossBot

            entity.kill()
