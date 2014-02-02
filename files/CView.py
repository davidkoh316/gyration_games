import Component
import View
import Globals
import math


class CView(Component.Component):
    def initialize(self, entity):
        pass
#        View.viewy = Globals.HEIGHT/2.0

    def update(self, entity, interval):
        if entity.faceRight:
            View.vcenterx = -View.centerOffset
        else:
            View.vcenterx = View.centerOffset

        x = entity.posx + entity.rect.width / 2.0
        vx = View.viewx + View.vcenterx
        if x - vx > View.vbr:
            View.viewx -= vx - x + View.vbr
        elif vx - x > View.vbr:
            View.viewx -= vx - x - View.vbr
        elif math.fabs(vx - x) > 0.1:
            View.viewx -= (vx - x) / 10.0

        if View.viewx < Globals.WIDTH / 2.0:
            View.viewx = Globals.WIDTH / 2.0

        y = entity.posy + entity.rect.width / 2.0
        if y - View.viewy > View.vbr:
            View.viewy -= View.viewy - y + View.vbr
        elif View.viewy - y > View.vbr:
            View.viewy -= View.viewy - y - View.vbr
        elif math.fabs(View.viewy - y) > 0.1:
            View.viewy -= (View.viewy - y) / 10.0

        if View.viewy > Globals.BOTTOM - Globals.HEIGHT / 2:
            View.viewy = Globals.BOTTOM - Globals.HEIGHT / 2
