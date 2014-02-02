import Component
import CSpawner
import math
import Globals


class CDespawn(Component.Component):
    def update(self, entity, interval):
        if math.fabs(Globals.PLAYER.posx - entity.posx) > CSpawner.RESET_LIMIT:
            entity.kill(False)
