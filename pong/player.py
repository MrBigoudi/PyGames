from entity import Entity

SPEED = 1024
MARGIN = 10
HEIGHT = 128
WIDTH = 32

MAX_GOALS = 10

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y, WIDTH, HEIGHT)
        self._speed = SPEED
        self._score = 0
    
    def moveDown(self, dt, maxHeight):
        self._y = min(maxHeight - self._height - MARGIN, max(MARGIN, self._y + self._speed * dt))
        # print(self._y)
    def moveUp(self, dt, maxHeight):
        self._y = min(maxHeight - self._height - MARGIN, max(MARGIN, self._y - self._speed * dt))

    def getScore(self):
        return self._score

    def score(self):
        self._score += 1

    def won(self):
        return self._score >= MAX_GOALS

    def collisionBall(self, ball):
        if (ball.getX() <= self._x + self._width) and (ball.getX() >= self._x):
            if (ball.getY() + ball.getHeight() >= self._y) and (ball.getY() <= self._y + self._height):
                ball.setVx(-ball.getVx())
            return
        if (ball.getX() + ball.getWidth() <= self._x + self._width) and (ball.getX() + ball.getWidth() >= self._x):
            if (ball.getY() + ball.getHeight() >= self._y) and (ball.getY() <= self._y + self._height):
                ball.setVx(-ball.getVx())
            return
        