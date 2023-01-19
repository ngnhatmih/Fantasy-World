from GameState import *
from TextureManager import *
from InputHandler import *

class MenuState(GameState):
    # State ID
    menuID = "MENU"
    vec = Vector2D([0,0])

    def __init__(self, game) -> None:
        self.game = game

    def update(self):
        for value in self.gameObjects.values():
            value.update()
            
        self.game.renderer.present()
        self.game.window.show()

    def render(self):
        self.game.renderer.clear()
        self.game.getRenderer().color = sdl2.ext.Color(*Colors.BLUE.value)
        self.gameObjects["penguin02"] = GameObject("test", self.vec.getX(), self.vec.getY(), 128, 128, 1.0, 1, self.game)
        for value in self.gameObjects.values():
            value.draw()

    def onEnter(self) -> bool:
        self.gameObjects["penguin01"] = GameObject("test", 50, 50, 128, 128, 1.0, 1, self.game)
        print("Entering menu state...")
        return True

    def onExit(self) -> bool:
        for value in self.gameObjects.values():
            value.clean()

        print("Exiting menu state...")
        return True
    
    def onKeyDown(self, event: sdl2.SDL_Event):
        pass

    def onKeyUp(self, event: sdl2.SDL_Event):
        pass

    def onMouseButtonDown(self, event: sdl2.SDL_Event):
        # Testing  
        self.onMouseMove(event)
        self.vec = InputHandler().getMousePos()
        print(f"Mouse Pos =", InputHandler().getMousePos())

    def onMouseButtonUp(self, event: sdl2.SDL_Event):
        pass

    def onMouseMove(self, event: sdl2.SDL_Event):
        # Update mouse's position
        InputHandler().mousePos.setX(event.motion.x)
        InputHandler().mousePos.setY(event.motion.y) 

    def getStateID(self) -> str:
        return self.menuID
