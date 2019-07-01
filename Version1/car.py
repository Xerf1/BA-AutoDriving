<<<<<<< HEAD

import pymunk
import pyglet
import resources
import math
from shapely.geometry import LineString
from shapely.geometry import *

debugVision = False
visualPoints = []
visionLinesNumber = 8
visionLinesDegrees = 360/visionLinesNumber


outerLine = LineString([(50,50), (50, 850), (1550,850), (1550, 500), (400, 500), (400, 400), (1550, 400), (1550, 50), (50,50)])
innerLine = LineString([(200,200), (200,700), (1400,700), (1400, 650), (250, 650), (250, 250), (1400, 250), (1400, 200), (200, 200)])


class Car (pymunk.Body):
    def __init__(self,space):
        super().__init__(10, pymunk.inf)
        self.position = 125, 125
        self.angle = 90/180 * math.pi
        self.shape = pymunk.Segment(self, (-12.5, 0), (+12.5, 0), 12.5)
        self.shape.elasticity = 0.98
        self.shape.collision_type = 1
        self.shape.color = 0,0,0,0
        self.sprite = pyglet.sprite.Sprite(resources.car_image)
        space.add(self, self.shape)

        self.gVelocity_x, self.gVelocity_y, self.velocity_x, self.velocity_y, self.cVelocity = 0.0, 0.0, 0.0, 0.0, 0.0
        if debugVision:
            self.loadVisiualPoints(space)

    def rotate(self, rot, dt):
        self.angle -= (rot * dt)/180 * math.pi

    def reset(self):
        self.position = 125,125
        self.angle = 90/180 * math.pi
        self.velocity = 0,0

    def loadVisiualPoints(self, space):
        for lineNr in range(visionLinesNumber):
            visualPoints.append(pymunk.Circle(pymunk.Body(0,0), 10, (0, 0)))
            space.add(visualPoints[lineNr])

    def updateVisionLines(self, space):
        for lineNr in range(visionLinesNumber):

            alpha = (-self.angle) + math.radians(lineNr * visionLinesDegrees)
            hypothenuse = 1600
            akathete = math.sin(alpha) * hypothenuse
            gkathete = math.cos(alpha) * hypothenuse

            x1 = self.position.x + akathete
            y1 = self.position.y + gkathete

            line = LineString([self.position, (x1, y1)])

            points = []

            IOL = outerLine.intersection(line)
            IIL = innerLine.intersection(line)

            if isinstance(IOL, Point):
                if isinstance(IIL, Point):
                    points.append((IOL.x, IOL.y))
                    points.append((IIL.x,IIL.y))
                if isinstance(IIL, MultiPoint):
                    points.append((IOL.x,IOL.y))

                    for point in IIL:
                        points.append((point.x, point.y))


            if isinstance(IOL, MultiPoint):
                if isinstance(IIL, Point):
                    points.append((IIL.x,IIL.y))

                    for point in IOL:
                        points.append((point.x, point.y))
                if isinstance(IIL, MultiPoint):
                    for point in IIL:
                        points.append((point.x, point.y))
                    for point in IOL:
                        points.append((point.x, point.y))


            if isinstance(IOL, GeometryCollection):
                if isinstance(IIL, MultiPoint):
                    for point in IIL:
                        points.append((point.x, point.y))
                if isinstance(IIL, Point):
                    points.append((IIL.x,IIL.y))

            if isinstance(IIL, GeometryCollection):
                if isinstance(IOL, MultiPoint):
                    for point in IOL:
                        points.append((point.x, point.y))
                if isinstance(IOL, Point):
                    points.append((IOL.x,IOL.y))


            while len(points) > 1:
                for p in points:
                    d = math.sqrt(math.pow(math.fabs(p[0]-self.position.x),2)+ math.pow(math.fabs(p[1]-self.position.y),2))
                    for p2 in points:
                        d2 = math.sqrt(math.pow(math.fabs(p2[0]-self.position.x),2)+ math.pow(math.fabs(p2[1]-self.position.y),2))
                        if d < d2:
                            points.remove(p2)


            """print(points)"""
            if debugVision:
                for p in points:
                    visualPoints[lineNr].body.position = (p[0], p[1])


    def update(self, dt):
        if self.cVelocity > 300:
            self.cVelocity = 300
        if self.cVelocity < -300:
            self.cVelocity = -300

        self.gVelocity_x = math.cos(self.angle) * self.cVelocity
        self.gVelocity_y = math.sin(self.angle) * self.cVelocity

        if self.velocity.x < self.gVelocity_x:
            self.velocity += 10,0
            if self.velocity.x > self.gVelocity_x:
                self.velocity = self.gVelocity_x, self.velocity.y

        if self.velocity.x > self.gVelocity_x:
            self.velocity -= 15,0
            if self.velocity.x < self.gVelocity_x:
                self.velocity = self.gVelocity_x, self.velocity.y

        if self.velocity.y < self.gVelocity_y:
            self.velocity += 0,10
            if self.velocity.y > self.gVelocity_y:
                self.velocity = self.velocity.x, self.gVelocity_y

        if self.velocity.y > self.gVelocity_y:
            self.velocity -= 0,15
            if self.velocity.y < self.gVelocity_y:
                self.velocity = self.velocity.x, self.gVelocity_y

        self.check_bounds()

        self.sprite.position = self.position.x, self.position.y
        self.sprite.rotation = math.degrees(-self.angle)
        self.update_position(self,dt)

        self.updateVisionLines(self.space)

    def check_bounds(self):
        min_x = 0
        min_y = 0
        max_x = 1600
        max_y = 900
        if self.position.x < min_x:
            self.position = max_x,self.position.y
        elif self.position.x > max_x:
            self.position = min_x,self.position.y
        if self.position.y < min_y:
            self.position = self.position.x, max_y
        elif self.position.y > max_y:
=======

import pymunk
import pyglet
import resources
import math




class Car (pymunk.Body):
    def __init__(self,space):
        super().__init__(10, pymunk.inf)
        self.position = 125, 200
        self.angle = 90/180 * math.pi
        self.shape = pymunk.Segment(self, (-12.5, 0), (+12.5, 0), 12.5)
        self.shape.elasticity = 0.98
        self.shape.collision_type = 2
        self.shape.color = 0,0,0,0
        self.sprite = pyglet.sprite.Sprite(resources.car_image)
        space.add(self, self.shape)

        self.gVelocity_x, self.gVelocity_y, self.velocity_x, self.velocity_y, self.cVelocity = 0.0, 0.0, 0.0, 0.0, 0.0

    def rotate(self, rot, dt):
        self.angle -= (rot * dt)/180 * math.pi

    def reset(self):
        self.position = 125,200
        self.angle = 90/180 * math.pi

    def update(self, dt):
        if self.cVelocity > 300:
            self.cVelocity = 300
        if self.cVelocity < -300:
            self.cVelocity = -300

        self.gVelocity_x = math.cos(self.angle) * self.cVelocity
        self.gVelocity_y = math.sin(self.angle) * self.cVelocity

        if self.velocity.x < self.gVelocity_x:
            self.velocity += 10,0
            if self.velocity.x > self.gVelocity_x:
                self.velocity = self.gVelocity_x, self.velocity.y

        if self.velocity.x > self.gVelocity_x:
            self.velocity -= 15,0
            if self.velocity.x < self.gVelocity_x:
                self.velocity = self.gVelocity_x, self.velocity.y

        if self.velocity.y < self.gVelocity_y:
            self.velocity += 0,10
            if self.velocity.y > self.gVelocity_y:
                self.velocity = self.velocity.x, self.gVelocity_y

        if self.velocity.y > self.gVelocity_y:
            self.velocity -= 0,15
            if self.velocity.y < self.gVelocity_y:
                self.velocity = self.velocity.x, self.gVelocity_y

        self.check_bounds()

        self.sprite.position = self.position.x, self.position.y
        self.sprite.rotation = math.degrees(-self.angle)
        self.update_position(self,dt)

    def check_bounds(self):
        min_x = 0
        min_y = 0
        max_x = 1600
        max_y = 900
        if self.position.x < min_x:
            self.position = max_x,self.position.y
        elif self.position.x > max_x:
            self.position = min_x,self.position.y
        if self.position.y < min_y:
            self.position = self.position.x, max_y
        elif self.position.y > max_y:
>>>>>>> 0e13d0c6f304902f2074cab7ccbea29ca4280fb4
            self.position = self.position.x, min_y