import pymunkoptions
pymunkoptions.options["debug"] = False
import pyglet
from pyglet.window import key
from pyglet.window import FPSDisplay
from pymunk.pyglet_util import DrawOptions
import math
import walls
import car
import pymunk
import coins

collision_types = {
    "car": 1,
    "wall":2,
}

dt = 1 / 120.0
turningSpeed = 200

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
        self.score = 0
        self.playerCar = car.Car(self.space)
        self.course = walls.Walls(self.space)
        self.coins = coins.Coins(self.space)
        self.fps = FPSDisplay(self)
        self.nearestCoinPos = self.coins.usedCoinPos[0]

        handler = self.space.add_collision_handler(1,2)
        handler.begin = self.hitWall


        coinHandler = self.space.add_collision_handler(1,3)
        coinHandler.begin = self.collectCoin

    def hitWall(self, arbiter, space, data):
        self.playerCar.reset()
        self.coins.respawnCoins(space)
        self.score = 0
        return True

    def collectCoin(self, arbiter, space, data):
        coin = arbiter.shapes[1]
        space.remove(coin, coin.body)
        self.coins.coinPos.append(coin.body.position)
        self.coins.usedCoinPos.remove(coin.body.position)
        self.score += 1
        for pos in self.coins.coinPos:
            coinDist = math.sqrt(math.pow(math.fabs(pos[0]-self.playerCar.position.x),2)+ math.pow(math.fabs(pos[1]-self.playerCar.position.y),2))
            if coinDist >= 300:
                self.coins.respawnCoin(self.space, pos)



        return True


    def on_draw(self):

        self.clear()
        self.space.debug_draw(self.options)
        self.label.draw()
        self.playerCar.sprite.draw()
        self.fps.draw()

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

        for pos in self.coins.usedCoinPos:
            coinDist = math.sqrt(math.pow(math.fabs(pos[0] - self.playerCar.position.x), 2) + math.pow(
                math.fabs(pos[1] - self.playerCar.position.y), 2))
            currentCoinDist = math.sqrt(
                math.pow(math.fabs(self.nearestCoinPos[0] - self.playerCar.position.x), 2) + math.pow(
                    math.fabs(self.nearestCoinPos[1] - self.playerCar.position.y), 2))

            if coinDist < currentCoinDist:
                self.nearestCoinPos = pos
            if self.nearestCoinPos not in self.coins.usedCoinPos:
                self.nearestCoinPos = pos

        self.label.text = str(self.nearestCoinPos)
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




if __name__ == '__main__':
    window = GameWindow(1600,900, "Game", resizable=False)
    pyglet.clock.schedule_interval(window.update, dt)
    pyglet.app.run()