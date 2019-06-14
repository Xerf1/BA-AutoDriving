
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
            self.position = self.position.x, min_y