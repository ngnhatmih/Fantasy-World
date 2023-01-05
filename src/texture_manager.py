import sdl2, sdl2.ext, sdl2.sdlimage
import ctypes
import pathlib
import sys

m_textureMap = {}
pTexture = None

class TextureManager:
    def __init__(self):
        pass
    

    @staticmethod
    def load(path: str, id: str, pRenderer: sdl2.ext.renderer.Renderer)->bool:


        pTexture: sdl2.ext.renderer.Texture = sdl2.sdlimage.IMG_LoadTexture(pRenderer.sdlrenderer, path)

        if pTexture != 0:
            m_textureMap[id] = pTexture
            return True
        else: return False

    @staticmethod
    def draw(id: str, x: int, y: int, width: int, height: int, scale: float, r: float, pRenderer: sdl2.ext.renderer.Renderer, flip: sdl2.SDL_RendererFlip):
        srcRect: sdl2.SDL_Rect = sdl2.SDL_RectEmpty
        destRect: sdl2.SDL_Rect = sdl2.SDL_RectEmpty

        srcRect.x = 0
        srcRect.y = 0
        srcRect.w = 0
        srcRect.h = 0
        destRect.x = 0
        destRect.y = 0
        destRect.w *= scale
        destRect.h *= scale

        pRenderer.copy(pTexture,srcRect,destRect)

    @staticmethod
    def drawFrame(id: str, x: int, y: int, width: int, height: int, scale: float, currentRow: int, currentFrame: int, r: float, pRenderer: sdl2.ext.renderer.Renderer, flip: sdl2.SDL_RendererFlip):
        srcRect: sdl2.SDL_Rect = sdl2.SDL_RectEmpty
        destRect: sdl2.SDL_Rect = sdl2.SDL_RectEmpty
        srcRect.x = width*currentFrame
        srcRect.y = height*currentRow
        srcRect.w = destRect.w = width
        srcRect.h = destRect.h = height
        destRect.x = x
        destRect.y = y
        destRect.w *= scale
        destRect.h *= scale

        pRenderer.copy(pTexture,srcRect,destRect)

    @staticmethod
    def cleanFromTextureMap(id : str):
        m_textureMap.pop(id)