import CSpawner
import World
import math
import Globals
import Entity
import CPhysics
import CAIRandom
import CAIFollow
import CCollision
import CLiving
import CDamage
import CDeathParticle
import CParticle
import CAnimation
import ImageManager
import pygame
import CDespawn


class CSpawnSlime(CSpawner.CSpawner):
    def update(self, entity, interval):
        distx = math.fabs(Globals.PLAYER.posx - entity.posx)
        if distx <= CSpawner.S_LIMIT and not self.activated:
            self.activated = True
            monster = Entity.Entity()
            monster.componentList.append(CAnimation.CAnimation(
                ImageManager.levelRes["three"]["Slimey_Sprite.png"], 2, 1, 0))
            monster.componentList.append(CPhysics.CPhysics())
            monster.componentList.append(CAIRandom.CAIRandom())
            monster.componentList.append(CCollision.CCollision())
            monster.componentList.append(CLiving.CLiving(22))
            monster.componentList.append(CDamage.CDamage(3))
            monster.componentList.append(CDeathParticle.CDeathParticle(
                ImageManager.levelRes["three"]["slimeydead.png"],
                3,
                (0, -20),
                CParticle.FLY_DOWNWARDS,
                pygame.BLEND_ADD))
            monster.componentList.append(CDespawn.CDespawn())

            World.groups["enemies"].add(monster)
            monster.initialize()
            monster.posx = entity.posx
            monster.posy = entity.posy

        elif self.activated and distx >= CSpawner.RESET_LIMIT:
            self.activated = False
