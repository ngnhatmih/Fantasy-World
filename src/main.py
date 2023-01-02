import sdl2, sdl2.ext
from constant import *

sdl2.ext.init()

window = sdl2.ext.Window("Title", size)
renderer = sdl2.ext.renderer.Renderer(window, flags = sdl2.SDL_RENDERER_ACCELERATED)

window.show()

isRunning = True
while isRunning:

    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_Quit:
            isRunning = False
        
    renderer.color = sdl2.ext.Color(*colors['white'], 0)
    renderer.clear()
    renderer.color = sdl2.ext.Color(*colors['violet'], 255)

    renderer.fill((100,100,100,100))

    renderer.present()

    window.refresh()

renderer.destroy()
window.close()
sdl2.ext.quit()
    