import pygame
from pygame.locals import *
import constants
from vector2f import Vector2f
import math
import wall

PLAYER_COLOR = (0, 255, 0, 255)
PLAYER_SPEED = 4
PLAYER_ROT = math.pi / 32

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([constants.TILE_WIDTH, constants.TILE_HEIGHT])
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x*constants.TILE_WIDTH
        self.rect.y = y*constants.TILE_HEIGHT
        # real player position
        self.x0 = self.rect.x + self.rect.width/2 # center of the player
        self.y0 = self.rect.y + self.rect.height/2
        # player position in the grid
        self.gX0, self.gY0 = Player.align_grid(self.x0, self.y0)
        # directions
        self.fov = math.pi / 3
        self.angle = math.pi / 4
        self.nbRays = 75
        self.rays = [0]*self.nbRays #rays direction vectors
        self.maxDepth = 512
        self.initRays()
        self.points = []


    def initRays(self):
        curAngle = self.angle - self.fov / 2
        delta = self.fov / self.nbRays
        for k in range(self.nbRays):
            # cosx = math.cos(curAngle) if math.cos(curAngle) else 1e-6
            # sinx = -math.sin(curAngle) if -math.sin(curAngle) else -1e6
            # ray = Vector2f(cosx,sinx)
            ray = curAngle
            curAngle += delta
            self.rays[k] = ray

    def align_grid(x,y):
        return ((x // constants.TILE_WIDTH) * constants.TILE_WIDTH, (y // constants.TILE_HEIGHT) * constants.TILE_HEIGHT)

    def checkInRightWalls(point, walls):
        for wall in walls:
            if (Player.chekInRightWall(point, wall)):
                return True
        return False
    def chekInRightWall(point, wall):
        return (point.x==wall[0]) and (wall[1]<=point.y and point.y<=wall[1]+constants.TILE_HEIGHT)
    
    def checkInLeftWalls(point, walls):
        for wall in walls:
            if (Player.chekInLeftWall(point, wall)):
                return True
        return False
    def chekInLeftWall(point, wall):
        return (point.x==wall[0]+constants.TILE_WIDTH) and (wall[1]<=point.y and point.y<=wall[1]+constants.TILE_HEIGHT)

    def checkInUpWalls(point, walls):
        for wall in walls:
            if (Player.chekInUpWall(point, wall)):
                return True
        return False
    def chekInUpWall(point, wall):
        return (point.y==wall[1]) and (wall[0]<=point.x and point.x<=wall[0]+constants.TILE_WIDTH)
    
    def checkInDownWalls(point, walls):
        for wall in walls:
            if (Player.chekInDownWall(point, wall)):
                return True
        return False
    def chekInDownWall(point, wall):
        return (point.y==wall[1]+constants.TILE_HEIGHT) and (wall[0]<=point.x and point.x<=wall[0]+constants.TILE_WIDTH)

    def cast(self, window, walls):
        points = []
        k = 0
        delta = constants.WINDOW_WIDTH / self.nbRays

        for ray in self.rays:
            # tangente of the ray's angle
            tanRay = math.tan(ray) 
            tanRay = tanRay if tanRay else 1e-6
            ptY = Vector2f()
            ptX = Vector2f()
            found = False

            #check vertically
            dx0 = 0 # the first vertical grid difference
            factor = 1
            # print("ray angle: ", ray)
            # if ray is facing right
            if (((-math.pi/2 <= ray) and (ray <= math.pi/2)) or ((3*math.pi/2 <= ray) and (ray <= 5*math.pi/2))):
                dx0 = self.gX0 + constants.TILE_WIDTH - self.x0
            # if ray is facing left
            else:
                dx0 = self.x0 - self.gX0
                factor = -1

            # iterate until hitting wall or depth max value
            for i in range(0, self.maxDepth, constants.TILE_WIDTH):
                deltaX = (dx0 + i)*factor
                x = self.x0 + deltaX
                # print("x: ",x)
                # the y position of the intersection
                y = self.y0 - (tanRay * deltaX)
                # print("y: ",y)
                pointTmp = Vector2f(x,y)

                # pygame.draw.circle(window, (0,0,255,255), (x,y), 4)

                # if the point is hitting a wall we add this point to the list of points
                if (factor == 1): # to compare to correct wall position
                    if Player.checkInRightWalls(pointTmp, walls):
                        ptX = pointTmp
                        found = True
                        break
                else:
                    if Player.checkInLeftWalls(pointTmp, walls):
                        ptX = pointTmp
                        found = True
                        break

            
            #check horizontally
            dy0 = 0 # the first horizontal grid difference
            factor = 1
            #print("ray angle: ", ray)
            # if ray is facing up
            if (((0 <= ray) and (ray <= math.pi)) or ((2*math.pi <= ray) and (ray <= 3*math.pi))):
                dy0 = self.y0 - self.gY0
                factor = -1
            # if ray is facing down
            else:
                dy0 = self.gY0 + constants.TILE_HEIGHT - self.y0

            # iterate until hitting wall or depth max value
            for i in range(0, self.maxDepth, constants.TILE_HEIGHT):
                deltaY = (dy0 + i)*factor
                y = self.y0 + deltaY
                # print("x: ",x)
                # the y position of the intersection
                x = self.x0 + ((self.y0-y)/tanRay)
                # print("y: ",y)
                pointTmp = Vector2f(x,y)

                # pygame.draw.circle(window, (0,255,0,255), (x,y), 4)

                # if the point is hitting a wall we add this point to the list of points
                if (factor == -1): # to compare to correct wall position
                    if Player.checkInDownWalls(pointTmp, walls):
                        ptY = pointTmp
                        found = True
                        break
                else:
                    if Player.checkInUpWalls(pointTmp, walls):
                        ptY = pointTmp
                        found = True
                        break

            if(found):
                # print(k, delta)
                player = Vector2f(self.x0, self.y0)
                distX = Vector2f.dist(ptX, player)
                distY = Vector2f.dist(ptY, player)
                lineH = 0
                lineOffset = 0

                if(ptX == Vector2f()):
                    points.append((ptY.x, ptY.y))
                    lineH = min(320,(wall.WALL_HEIGHT*320/distY))
                    lineOffset = constants.WINDOW_HEIGHT/2 - lineH/2
                    rect = pygame.Rect(k*delta,lineOffset,delta+1,lineH)
                    pygame.draw.rect(window, (123,23,42), rect)
                    k += 1
                    continue

                if(ptY == Vector2f()):
                    points.append((ptX.x, ptX.y))
                    lineH = min(320,(wall.WALL_HEIGHT*320/distX))
                    lineOffset = constants.WINDOW_HEIGHT/2 - lineH/2
                    rect = pygame.Rect(k*delta,lineOffset,delta+1,lineH)
                    pygame.draw.rect(window, (123,23,42), rect)
                    k += 1
                    continue

                # print(str(ptX), str(ptY))
                if (distX < distY) :
                    points.append((ptX.x, ptX.y))
                    lineH = min(320,(wall.WALL_HEIGHT*320/distX))
                    lineOffset = constants.WINDOW_HEIGHT/2 - lineH/2
                else:
                    points.append((ptY.x, ptY.y))
                    lineH = min(320,(wall.WALL_HEIGHT*320/distY))
                    lineOffset = constants.WINDOW_HEIGHT/2 - lineH/2
                # print(k,delta)
                rect = pygame.Rect(k*delta,lineOffset,delta+1,lineH)
                pygame.draw.rect(window, (123,23,42), rect)

            k += 1
        # print(points)
        self.points = points

        return points


    def drawRays(self, window):
        origin = (self.rect.x + self.rect.width/2 , self.rect.y  + self.rect.height/2 )
        for point in self.points:
            # print(point)
            pygame.draw.line(window, (0,255,255), origin, point)

    def move(self, group):
        curX = self.rect.x
        curY = self.rect.y
        self.rect.y -= PLAYER_SPEED*math.sin(self.angle)
        self.rect.x += PLAYER_SPEED*math.cos(self.angle)
        if(self.isColliding(group)):
            self.rect.x = curX
            self.rect.y = curY
        self.x0 = self.rect.x + self.rect.width/2 # center of the player
        self.y0 = self.rect.y + self.rect.height/2
        # player position in the grid
        self.gX0, self.gY0 = Player.align_grid(self.x0, self.y0)

    def rotateLeft(self):
        self.angle = (self.angle+PLAYER_ROT) % (2*math.pi)
        self.initRays()
    def rotateRight(self):
        self.angle = (self.angle-PLAYER_ROT) % (2*math.pi)
        self.initRays()

    def draw(self, window):
        pygame.draw.rect(window, PLAYER_COLOR, self.rect)
        self.drawRays(window)

    def isColliding(self, group):
        if pygame.sprite.spritecollide(self, group, False):
            return True
        return False

    def update(self, keys, group):
        if (K_w in keys) or (K_UP in keys):
            self.move(group)
        if K_LEFT in keys:
            self.rotateRight()
        if K_RIGHT in keys:
            self.rotateLeft()