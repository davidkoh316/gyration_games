import Component
import math
import Globals
import pygame


class CSun(Component.Component):
    def update(self, entity, interval):
#        distx = Globals.PLAYER.posx - entity.posx
#        disty = Globals.PLAYER.posy - entity.posy
#        dist = math.sqrt(distx * distx + disty * disty)
#        if dist <= 50:
        if not Globals.PLAYER is None and\
                pygame.sprite.collide_rect(entity, Globals.PLAYER):
            entity.kill()
            Globals.MINI_SUNS = Globals.MINI_SUNS + 1
            Globals.MINI_SUNS_INLVL = Globals.MINI_SUNS_INLVL + 1
            Globals.SCORE = Globals.SCORE + 1000
            sunID = Globals.sunPos()[(entity.rect.x, entity.rect.y)]
            Globals.sunTr()[sunID] = False
