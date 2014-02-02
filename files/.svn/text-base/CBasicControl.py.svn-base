import pygame
import InputManager
import Component
import World
import Entity
import ImageManager
import CAnimation
import CPhysics
import CAttach
import CCollision
import CDamage
import CProjectile
import Globals

MOVE_AMOUNT = 200.0
#JUMP_AMOUNT = 610.0


class CBasicControl(Component.Component):
    def initialize(self, entity):
        self.bowCooldown = 0.0

    def update(self, entity, interval):
        if entity.stunTimeout > 0:
            entity.state = 5
            entity.sAnim = 0
            if entity.isGrounded:
                entity.velx = 0
        else:
            if InputManager.getPressed("attack1") and not entity.isAttacking:
                if entity.equipType == CAttach.ZORD:
                    entity.state = 4
                    entity.sAnim = 0
                    entity.asAnimEnd = 2
                elif entity.equipType == CAttach.BOW and\
                        self.bowCooldown == 0.0:
                    entity.state = 3
                    entity.sAnim = 0
                    entity.asAnimEnd = 2

                    aimg = ImageManager.levelRes["player"]["Arrow.png"]
                    if entity.faceRight:
                        vel = Globals.ARROW_VELOCITY
                    else:
                        vel = -Globals.ARROW_VELOCITY
                        aimg = pygame.transform.flip(aimg, True, False)
                    arrow = Entity.Entity()
                    arrow.componentList.append(CPhysics.CPhysics())
                    arrow.componentList.append(CCollision.CCollision())
                    arrow.componentList.append(CProjectile.CProjectile(
                        aimg,
                        (entity.posx + 3.0, entity.posy + 60.0),
                        (vel, -5.0),
                        (0.0, 9.0),
                        Globals.ARROW_HITS))
                    arrow.componentList.append(
                        CDamage.CDamage(Globals.ARROW_DAMAGE))
                    arrow.initialize()
                    World.groups["pProjectile"].add(arrow)
                    self.bowCooldown = Globals.BOW_COOLDOWN
                entity.isAttacking = True
            if InputManager.getAction("left"):
                entity.velx = - MOVE_AMOUNT
                if entity.isGrounded and not entity.isAttacking:
                    entity.state = 1
                entity.faceRight = False
            elif InputManager.getAction("right"):
                entity.velx = MOVE_AMOUNT
                if entity.isGrounded and not entity.isAttacking:
                    entity.state = 1
                entity.faceRight = True
            elif not entity.isAttacking:
                entity.velx = 0
                if entity.isGrounded:
                    entity.state = 0
            if InputManager.getPressed("jump") and\
                    entity.isGrounded and not entity.isAttacking:
                entity.vely = - Globals.PLAYER_JUMP
                entity.isGrounded = False
                entity.state = 2
            if InputManager.getPressed("sword"):
                World.groups["equipment"].empty()

                zord = Entity.Entity()
                zord.componentList.append(CAnimation.CAnimation(
                    ImageManager.levelRes["player"]["Zord_Spritesheet.png"],
                    6, 6, 0, 0))
                zord.componentList.append(CPhysics.CPhysics())
                zord.accy = 0
                zord.componentList.append(CAttach.CAttach(entity, 53))
                World.groups["equipment"].add(zord)
                zord.initialize()
            elif InputManager.getPressed("bow"):
                World.groups["equipment"].empty()

                bow = Entity.Entity()
                bow.componentList.append(CAnimation.CAnimation(
                    ImageManager.levelRes[
                        "player"]["BowArrow_Spritesheet.png"],
                    6, 6, 0, 0))
                bow.componentList.append(CPhysics.CPhysics())
                bow.accy = 0
                bow.componentList.append(
                    CAttach.CAttach(entity, 28, CAttach.BOW))
                World.groups["equipment"].add(bow)
                bow.initialize()
        self.bowCooldown -= interval
        if self.bowCooldown < 0.0:
            self.bowCooldown = 0.0
