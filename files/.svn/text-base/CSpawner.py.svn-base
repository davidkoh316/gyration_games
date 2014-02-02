import Component


S_LIMIT = 600
RESET_LIMIT = 700


class CSpawner(Component.Component):
    def __init__(self, amount=1):
        self.amount = amount
        self.activated = False

    def update(self, entity, interval):
        distx = math.fabs(Globals.PLAYER.posx - entity.posx)
        if distx <= S_LIMIT and not self.activated:
            self.activated = True
        elif self.activated and distx >= RESET_LIMIT:
            self.activated = False
