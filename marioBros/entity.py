class Entity:

    def __init__(self, x, y, width, height, texture):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._texture = texture

    # getters
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getHeight(self):
        return self._height
    def getWidth(self):
        return self._width
    def getTexture(self):
        return self._texture