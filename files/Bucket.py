

class Bucket(object):
    def __init__(self, x, y):
        self.objs = set()
        self.x = x
        self.y = y

    def empty(self):
        self.objs = set()

    def add(self, obj):
        self.objs.add(obj)

    def objects(self):
        return self.objs
