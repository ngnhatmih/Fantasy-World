import sdl2, sdl2.ext
import InputHandler
from TextureManager import *
from Constant import *
from GameStateMachine import *
from MenuState import MenuState


class Singleton(type):
    # __call__ makes the class itself become a function whenever it is called
    def __call__(self, *args, **kwds):
        # Check whether the instance is in instances
        if self not in self.instances:
            instance = super().__call__(*args, **kwds)
            self.instances[self] = instance
        return self.instances[self]  

class Game(metaclass = Singleton):
    version = 0.0
    # This variable is used to store all instances initialized
    instances = {}
    # This machine helps push, pop or change state
    gameStateMachine= GameStateMachine()

    def __init__(self):
        # Initialize SDL and its subsystems
        # Subsystems (default): video=True, audio=False, timer=False, joystick=False,
        # controller=False, haptic=False, sensor=False, events=True
        sdl2.ext.init()

        # Push menu state
        self.gameStateMachine.pushState(MenuState(self))

        # Window Creation
        self.window = sdl2.ext.Window(f"Fantasy-World {self.version}", SIZE)

        # Renderer Creation
        self.renderer = sdl2.ext.renderer.Renderer(self.window, flags = sdl2.SDL_RENDERER_ACCELERATED)

        # Show the windows
        self.window.show() 

        # Is the game running?
        self.isRunning = True

        # Load the textures
        TextureManager().load("assets/textures/red.png", "test", self.renderer)
        self.currentFrame = 0

    # Get the machine through Game()
    def getGameStateMachine(self)-> gameStateMachine:
        return self.gameStateMachine
        
    # Event Handling
    def eventHandle(self):
        self.isRunning = InputHandler.InputHandler(self).update()

    # Render the frame
    def render(self):
        self.renderer.clear()
        self.gameStateMachine.render()

    # Update to the screen
    def update(self):
        self.gameStateMachine.update()
    
    # Clean up
    def clean(self):
        self.window.close()
        self.renderer.destroy()
        sdl2.ext.quit()