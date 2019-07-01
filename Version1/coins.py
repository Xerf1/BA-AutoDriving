import pymunk

class Coins (pymunk.Body):
    def __init__(self, space):
        super().__init__(10, pymunk.inf)
        self.thickness = 4


        self.usedCoinPos = []
        self.coinPos = []

        self.coinPos.append((125, 200))
        self.coinPos.append((125, 300))
        self.coinPos.append((125, 400))
        self.coinPos.append((125, 500))
        self.coinPos.append((125, 600))
        self.coinPos.append((125, 700))
        self.coinPos.append((200, 775))
        self.coinPos.append((300, 775))
        self.coinPos.append((400, 775))
        self.coinPos.append((500, 775))
        self.coinPos.append((600, 775))
        self.coinPos.append((700, 775))
        self.coinPos.append((800, 775))
        self.coinPos.append((900, 775))
        self.coinPos.append((1000, 775))
        self.coinPos.append((1100, 775))
        self.coinPos.append((1200, 775))
        self.coinPos.append((1300, 775))
        self.coinPos.append((1400, 775))
        self.coinPos.append((1475, 675))
        self.coinPos.append((1400, 575))
        self.coinPos.append((1300, 575))
        self.coinPos.append((1200, 575))
        self.coinPos.append((1100, 575))
        self.coinPos.append((1000, 575))
        self.coinPos.append((900, 575))
        self.coinPos.append((800, 575))
        self.coinPos.append((700, 575))
        self.coinPos.append((600, 575))
        self.coinPos.append((500, 575))
        self.coinPos.append((400, 575))
        self.coinPos.append((325, 450))
        self.coinPos.append((400, 325))
        self.coinPos.append((500, 325))
        self.coinPos.append((600, 325))
        self.coinPos.append((700, 325))
        self.coinPos.append((800, 325))
        self.coinPos.append((900, 325))
        self.coinPos.append((1000, 325))
        self.coinPos.append((1100, 325))
        self.coinPos.append((1200, 325))
        self.coinPos.append((1300, 325))
        self.coinPos.append((1400, 325))
        self.coinPos.append((1475, 225))
        self.coinPos.append((1400, 125))
        self.coinPos.append((1300, 125))
        self.coinPos.append((1200, 125))
        self.coinPos.append((1100, 125))
        self.coinPos.append((1000, 125))
        self.coinPos.append((900, 125))
        self.coinPos.append((800, 125))
        self.coinPos.append((700, 125))
        self.coinPos.append((600, 125))
        self.coinPos.append((500, 125))
        self.coinPos.append((400, 125))
        self.coinPos.append((300, 125))
        self.coinPos.append((200, 125))

        for cPos in self.coinPos:
            body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
            body.position = cPos
            shape = pymunk.Circle(body,10,(0,0))
            shape.elasticity = 0
            shape.density = 0.001
            shape.collision_type = 3
            space.add(body,shape)
            self.usedCoinPos.append(cPos)



        self.coinPos.clear()

    def respawnCoins(self,space):

        for cPos in self.coinPos:
            body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
            body.position = cPos
            shape = pymunk.Circle(body,10,(0,0))
            shape.elasticity = 0
            shape.density = 0.001
            shape.collision_type = 3
            space.add(body,shape)
            self.usedCoinPos.append(cPos)

        self.coinPos.clear()

    def respawnCoin(self, space, cPos):


        body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        body.position = cPos
        shape = pymunk.Circle(body, 10, (0, 0))
        shape.elasticity = 0
        shape.density = 0.001
        shape.collision_type = 3
        space.add(body, shape)
        self.usedCoinPos.append(cPos)
        self.coinPos.remove(cPos)