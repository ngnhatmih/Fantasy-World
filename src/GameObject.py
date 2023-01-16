import sdl2, sdl2.ext
from Vector2D import *
from TextureManager import *

class GameObject:

    def __init__(self, textureID, x, y, w, h, scale, numFrames, game):
        self.rect: sdl2.ext.surface.SDL_Rect = (x, y, w, h)
        self.pos = self.vel = Vector2D([0,0])
        self.scale = 1
        self.curRow = 0
        self.curFrame = 0
        self.numFrames = numFrames
        self.rotate = 0.0
        self.textureID = textureID
        self.game = game

    def draw(self):
        TextureManager().drawFrame(self.game.renderer, self.textureID, self.rect[0], self.rect[1], self.rect[2], self.rect[3], self.scale, self.curFrame, self.curRow)

    def update(self): 
        self.pos += self.vel

        self.rect = (self.pos.getX(), self.pos.getX(), self.rect[2], self.rect[3])

    def clean(self): pass

    def getW(self): return self.rect.w

    def getH(self): return self.rect.h

    def getPos(self)->Vector2D: return self.pos

    def getTextureID(self)->str: return self.textureID

    def checkCollision(self, vec: Vector2D)->bool: 
        if (vec.getX() < self.pos.getX() + self.getW 
            and vec.getY() > self.pos.getY()
            and vec.getX() < self.pos.getX() + self.getH):
            return True
            
        else: return False

