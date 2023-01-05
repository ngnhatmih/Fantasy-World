import sdl2
import sdl2.ext
import sdl2.sdlimage
import ctypes
import pathlib
import sys


textureMap = {}


class TextureManager:
    def __init__(self):
        pass

    @staticmethod
    def load(path: str, id: str, renderer: sdl2.ext.renderer.Renderer) -> bool:
        # Use the built-in pysdl2 image loading library instead of the C version
        # Still returns the C SDL_Surface though
        # This also initializes the SDL image library for us
        surface: sdl2.SDL_Surface = sdl2.ext.image.load_img(path)

        if surface == 0:
            return False

        # Add the texture to the texture list
        textureMap[id] = sdl2.ext.Texture(renderer, surface)

        # We can now free the surface since the texture is now stored in sdl2.ext.Texture
        sdl2.SDL_FreeSurface(surface)

        return True


    @staticmethod
    def draw(renderer: sdl2.ext.renderer.Renderer, id: str, x: int, y: int, width: int, height: int, currentRow: int = 0, currentFrame: int = 0, scaleX: float = 1, scaleY: float = 1):
        srcRect = (width*currentFrame, height*currentRow, width, height)
        destRect = (x, y, width*scaleX, height*scaleY)

        renderer.copy(textureMap[id], srcRect, destRect)

    @staticmethod
    def cleanFromTextureMap(id: str):
        textureMap.pop(id)
