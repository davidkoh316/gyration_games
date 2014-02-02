import Component
import Globals
import InputManager
import CSpawnSnowboss
import World
import Entity
import pygame
import ImageManager


class CPlayer(Component.Component):
    """Player component for player specific events
        (Reaching end of level, etc.)"""
    def initialize(self, entity):
        entity.regen_time = 0.0
        entity.mp = Globals.PLAYER_MAX_MP

    def update(self, entity, interval):
        if entity.posx > Globals.WIN_POS:
            Globals.WIN = True
        entity.regen_time += interval
        if entity.regen_time >= Globals.PLAYER_REGEN_TIME:
            if entity.health < Globals.PLAYER_MAX_HEALTH:
                entity.health += 1
            if entity.mp < Globals.PLAYER_MAX_MP:
                entity.mp += 1
            entity.regen_time = 0.0
        if InputManager.getPressed("debugMode"):
            Globals.DEBUG_MODE = not Globals.DEBUG_MODE
        if InputManager.getAction("cheat1") and Globals.DEBUG_MODE:
            entity.health = Globals.PLAYER_MAX_HEALTH
        if InputManager.getPressed("cheat2") and Globals.DEBUG_MODE:
            Globals.WIN = True
            if Globals.CURRENT_LEVEL == "five":
                Globals.GAMECOMPLETED = True
        if InputManager.getPressed("cheat3") and Globals.DEBUG_MODE:
            Globals.MINI_SUNS += 1
        if InputManager.getPressed("cheatPos") and Globals.DEBUG_MODE:
            print Globals.PLAYER.rect.x, Globals.PLAYER.rect.y
#        if InputManager.getPressed("cheatboss"):
#            ImageManager.loadSet("boss")
#            bossSpawn = Entity.Entity()
#            bossSpawn.componentList.append(CSpawnSnowboss.CSpawnSnowboss())
#            World.groups["spawners"].add(bossSpawn)
#            bossSpawn.initialize()
#            bossSpawn.posx = entity.posx
#            bossSpawn.posy = entity.posy
#            bossSpawn.rect = pygame.Rect(0, 0, 40, 40)
