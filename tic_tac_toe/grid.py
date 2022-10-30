import numpy as np
import pygame

class Grid:

    size = 3
    cellWidth = 256
    cellHeight = 256
    margin = 2
    p1 = 1
    p2 = 2

    def __init__(self):
        self._state = np.zeros((Grid.size, Grid.size))
        w, h = pygame.display.get_surface().get_size()
        self._x = w // 2 - (Grid.size / 2 * Grid.cellWidth)
        self._y = h // 2 - (Grid.size / 2 * Grid.cellHeight)


    def drawCell(self, window, i, j):
        rectP = pygame.Rect(self._x + i*Grid.cellWidth + Grid.margin, self._y + j*Grid.cellWidth + Grid.margin, Grid.cellWidth - 2*Grid.margin, Grid.cellHeight - 2*Grid.margin)
        rect = pygame.Rect(self._x + i*Grid.cellWidth, self._y + j*Grid.cellWidth, Grid.cellWidth, Grid.cellHeight)
        if(self._state.item((i,j)) == Grid.p1):
            pygame.draw.rect(window, pygame.Color("red") ,rectP)
        elif(self._state.item((i,j)) == Grid.p2):
            pygame.draw.rect(window, pygame.Color("green") ,rectP)
        else:
            pygame.draw.rect(window, pygame.Color("white") ,rect, Grid.margin)


    def draw(self, window):
        for i in range(Grid.size):
            for j in range(Grid.size):
                self.drawCell(window, i, j)


    def set(self, i, j, p):
        self._state[i,j] = p

    def getGrid(self):
        return self._state

    def getPos(self):
        return (self._x, self._y)

    def checkFull(self):
        for rows in self._state:
            for e in rows:
                if e == 0:
                    return False
        return True


    def checkRaw(self, p, i):
        for j in range(Grid.size):
            if self._state[i,j] != p:
                return False
        return True

    def checkRaws(self, p):
        for i in range(Grid.size):
            if(self.checkRaw(p, i)):
                return True
        return False


    def checkCol(self, p, j):
        for i in range(Grid.size):
            if self._state[i,j] != p:
                return False
        return True

    def checkCols(self, p):
        for j in range(Grid.size):
            if(self.checkCol(p, j)):
                return True
        return False

    def checkFstDiag(self, p):
        for i in range(Grid.size):
            for j in range(Grid.size):
                if(i != j):
                    continue
                if self._state[i,j] != p:
                    return False
        return True


    def checkSndDiag(self, p):
        for i in range(Grid.size):
            for j in range(Grid.size):
                if(i != Grid.size - 1 - j):
                    continue
                if self._state[i,j] != p:
                    return False
        return True


    def checkWinP(self, p):
        return self.checkCols(p) or self.checkRaws(p) or self.checkFstDiag(p) or self.checkSndDiag(p)


    # returnf -1, p1 or p2
    def checkWin(self):
        if(self.checkWinP(Grid.p1)):
            return Grid.p1
        if(self.checkWinP(Grid.p2)):
            return Grid.p2
        return -1