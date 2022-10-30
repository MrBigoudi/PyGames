from movingEntity import MovingEntity

class Mario(MovingEntity):

    def __init__(self, x, y, width, height, texture, vx, vy):
        MovingEntity(self, x, y, width, height, texture, vx, vy)
        self._lives = 5