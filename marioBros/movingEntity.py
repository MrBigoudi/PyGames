from entity import Entity

class MovingEntity(Entity):

    def __init__(self, x, y, width, height, texture, vx, vy):
        Entity.__init__(self, x, y, width, height, texture)
        self._vx = vx
        self._vy = vy

    # getters
    def getVx(self):
        return self._vx
    def getVy(self):
        return self._vy