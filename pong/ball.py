from entity import Entity

WIDTH = 16
HEIGHT = 16

INIT_VX = 720
INIT_VY = 720

INIT_CPT = 0

class Ball(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y, WIDTH, HEIGHT)
        self._initX = x
        self._initY = y
        self._vx = INIT_VX
        self._vy = INIT_VY
        self._cpt = INIT_CPT

    def init(self):
        self._x = self._initX
        self._y = self._initY
        # change direction but reset speed
        self._vx = -((self._vx / abs(self._vx))*INIT_VX)
        self._vy = ((self._vy / abs(self._vy))*INIT_VY)
        self._cpt = INIT_CPT


    def setVx(self, newVx):
        self._vx = newVx
    def setVy(self, newVy):
        self._vy = newVy
    def setSpeed(self, vx, vy):
        self.setVx(vx)
        self.setVy(vy)
    def getVx(self):
        return self._vx
    def getVy(self):
        return self._vy

    def update(self, dt, maxHeight, maxWidth):
        self._cpt += 1e-5
        self._y = min(maxHeight - 2*self._height, max(self._height, self._y + self._vy * (dt + self._cpt)))
        self._x = min(maxWidth - 2*self._width, max(self._width, self._x + self._vx * (dt + self._cpt)))
        # change direction
        if (self._y <= self._height) or (self._y >= (maxHeight - 2*self._height)):
            # print("test", maxHeight)
            self.setVy(-self._vy)

        Entity.update(self, dt)

        # check goals
        if (self._x <= self._width):
            self.init()
            return 1
        elif (self._x >= (maxWidth - 2*self._width)):
            self.init()
            return -1
        return 0