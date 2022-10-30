from game_object import GameObject

class MovingObject(GameObject):
    # constructor
    def __init__(self, x, y, width, height, colour, vx, vy):
        # speed
        self._vx = vx
        self._vy = vy
        # parent
        GameObject.__init__(self, x, y, width, height, colour)

    def moveUp(self, speed):
        GameObject._setY(self, self._y-speed)
    def moveDown(self, speed):
        GameObject._setY(self, self._y+speed)
    def moveLeft(self, speed):
        GameObject._setX(self, self._x-speed)
    def moveRight(self, speed):
        GameObject._setX(self, self._x+speed)

    def toString(self):
        return GameObject.toString(self) + "\nvx: " + str(self._vx) + "\nvy: " + str(self._vy)