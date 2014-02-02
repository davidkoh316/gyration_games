import Component


class CTimedDespawn(Component.Component):
    def __init__(self, time):
        self.time = time

    def update(self, entity, interval):
        self.time -= interval
        if self.time <= 0.0:
            entity.kill()
