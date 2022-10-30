from moving_object import MovingObject
from random import randint
import globals

class Pipe(MovingObject):
    
    colour = (0,255,0,255)
    width = 64
    vx = 4
    space_h = 256
    space_w = 512
    min_height = 16
    sId = 0

    def __init__(self, x, y, height):
        MovingObject.__init__(self, x, y, Pipe.width, height, Pipe.colour, Pipe.vx, 0)
        Pipe.sId += 1
        self.id = Pipe.sId

    
    def updateList(pipeList):
        for pipe in pipeList:
            pipe.moveLeft(Pipe.vx)
        Pipe.genInfinitePipe(pipeList)

    def createPipes(x):
        p1Height = randint(Pipe.min_height, globals.WINDOW_HEIGHT // 2)
        p_haut = Pipe(x, 0, p1Height)
        p_bas = Pipe(x, p1Height + Pipe.space_h, globals.WINDOW_HEIGHT)
        return (p_haut,p_bas)

    def checkPipeInScreen(self):
        return self._x + Pipe.width > 0

    def checkPipesInScreen(pipeList):
        for pipe in pipeList:
            if(not pipe.checkPipeInScreen()):
                pipeList.remove(pipe)

    def drawList(pipeList, window):
        for pipe in pipeList:
            pipe.draw(window)

    def addPipes(pipeList):
        (p1,p2) = Pipe.createPipes(globals.WINDOW_WIDTH)
        pipeList.append(p1)
        pipeList.append(p2)

    def genInfinitePipe(pipeList):
        # on check si des tuyaux doivent etre enleves
        Pipe.checkPipesInScreen(pipeList)
        size = len(pipeList)
        # si la liste est vide on ajoute un tuyau
        if size == 0:
            Pipe.addPipes(pipeList)
        # sinon on la remplie
        else:
            # on regarde la position du dernier tuyau
            x = pipeList[size - 1].getX()
            # s'il est trop proche du bord on attend sinon on ajoute un nouveau tuyau
            if x < globals.WINDOW_WIDTH - Pipe.space_w:
                Pipe.addPipes(pipeList)

