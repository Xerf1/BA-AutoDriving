import pymunkoptions
pymunkoptions.options["debug"] = False
import pyglet
from pyglet.window import key
from pymunk.pyglet_util import DrawOptions
import resources
import math
import physicalobject
import walls
import car
import pymunk

collision_types = {
    "car": 1,
    "wall":2,
}




class GameWindow(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.keysDown = []
        self.label = pyglet.text.Label("test",
                          font_name='Times New Roman',
                          font_size=36,
                          x=self.width//2, y=self.height//2,
                          anchor_x='center', anchor_y='center')

        self.space = pymunk.Space()
        self.options = DrawOptions()

        self.playerCar = car.Car(self.space)
        self.course = walls.Walls(self.space)

        self.playerCar.shape.collision_type = 1
        self.course.w1.collision_type = 2

        handler = self.space.add_default_collision_handler()
        handler.begin = self.hitWall

    def hitWall(self, arbiter, space, data):
        self.playerCar.reset()
        return True


    def on_draw(self):
        self.clear()
        self.space.debug_draw(self.options)
        self.label.draw()
        self.playerCar.sprite.draw()

    def update(self, dt):
        self.space.step(dt)
        self.playerCar.update(dt)
        if "W" in self.keysDown:
            self.playerCar.cVelocity += 10
        elif "W" not in self.keysDown and self.playerCar.cVelocity > 0:
            self.playerCar.cVelocity = 0

        if "S" in self.keysDown:
            self.playerCar.cVelocity -= 10
        elif "S" not in self.keysDown and self.playerCar.cVelocity < 0:
            self.playerCar.cVelocity = 0

        if "D" in self.keysDown:
            self.playerCar.rotate(turningSpeed, dt)

        if "A" in self.keysDown:
            self.playerCar.rotate(-turningSpeed, dt)

        self.label.text = str(self.keysDown)
        self.space.reindex_shapes_for_body(self.playerCar)

    def on_key_press(self, symbol,modifiers):
        if symbol == key.D:
            self.keysDown.append("D")
        if symbol == key.A:
            self.keysDown.append("A")
        if symbol == key.W:
            self.playerCar.cVelocity = math.sqrt(self.playerCar.velocity_x ** 2 + self.playerCar.velocity_y ** 2)
            self.keysDown.append("W")
        if symbol == key.S:
            self.playerCar.cVelocityaaa = math.sqrt(self.playerCar.velocity_x ** 2 + self.playerCar.velocity_y ** 2)
            self.keysDown.append("S")
        pass

    def on_key_release(self, symbol, modifiers):
        if symbol == key.D:
            self.keysDown.remove("D")
        if symbol == key.A:
            self.keysDown.remove("A")
        if symbol == key.W:
            self.keysDown.remove("W")
        if symbol == key.S:
            self.keysDown.remove("S")
        pass


"game_window = pyglet.window.Window(1600, 900)"
dt = 1/120.0
turningSpeed = 200
"""player_car = physicalobject.PhysicalObject(
	img=resources.car_image, x=800, y=450)"""



"""space = pymunk.Space()"""

"""wall = walls.Walls(space)"""

"""label = pyglet.text.Label("test",
                          font_name='Times New Roman',
                          font_size=36,
                          x=game_window.width//2, y=game_window.height//2,
                          anchor_x='center', anchor_y='center')"""



"""def update(dt):
    player_car.update(dt)
    if "W" in keysDown:
        player_car.velocity += 10
    elif "W" not in keysDown and player_car.velocity > 0:
        player_car.velocity = 0

    if "S" in keysDown:
        player_car.velocity -= 10
    elif "S" not in keysDown and player_car.velocity < 0:
        player_car.velocity = 0

    if "D" in keysDown:
        player_car.rotate(turningSpeed, dt)

    if "A" in keysDown:
        player_car.rotate(-turningSpeed, dt)

    label.text = str(player_car.velocity_x)"""


"""@window.event"""




""""@game_window.event"""
"""def on_draw():
    "game_window.clear()"
    player_car.draw()
    "label.draw()"""

if __name__ == '__main__':
    window = GameWindow(1600,900, "Game", resizable=False)
    pyglet.clock.schedule_interval(window.update, dt)
    pyglet.app.run()