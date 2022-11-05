import math

class Vector2f:
    
    def __init__(self, x : float = 0., y : float = 0., *, v = 0):
        if(v):
            self.x = v.x
            self.y = v.x
            return
        self.x = x
        self.y = y

    def abs(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def absSquared(self) -> float:
        return self.abs()**2

    def translate(self, x, y):
        self.x += x
        self.y += y

    def normalize(self):
        norm = self.abs()
        self.x = self.x / norm
        self.y = self.y / norm

    def normalized(self):
        norm = self.abs()
        x = self.x / norm
        y = self.y / norm
        return Vector2f(x,y)

    def negate(self):
        self.x = -self.x
        self.y = -self.y

    def normal(self):
        return Vector2f(-self.y, self.x)

    def dist(v1, v2):
        return math.sqrt((v1.x-v2.x)**2 + (v1.y-v2.y)**2)

    # products
    def dot(self, v2) -> float:
        return self.x * v2.x + self.y * v2.y


    # component wise operators
    def __add__(self, v2):
        return Vector2f(self.x + v2.x, self.y + v2.y)
    def __sub__(self, v2):
        return Vector2f(self.x - v2.x, self.y - v2.y)
    def __mul__(self, v2):
        return Vector2f(self.x * v2.x, self.y * v2.y)
    def __truediv__(self, v2):
        return Vector2f(self.x / v2.x, self.y / v2.y)
    def __eq__(self, v2):
        return self.x==v2.x and self.y==v2.y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"