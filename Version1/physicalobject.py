import pyglet
import math

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gVelocity_x, self.gVelocity_y, self.velocity_x, self.velocity_y, self.velocity = 0.0, 0.0, 0.0, 0.0, 0.0

    def rotate(self, rot, dt):
        self.rotation += rot * dt

    def update(self, dt):

        self.gVelocity_x = math.cos(-(self.rotation/180) * math.pi) * self.velocity
        self.gVelocity_y = math.sin(-(self.rotation/180) * math.pi) * self.velocity

        if self.velocity_x < self.gVelocity_x:
            self.velocity_x += 20

        if self.velocity_x > self.gVelocity_x:
            self.velocity_x -= 20

        if self.velocity_y < self.gVelocity_y:
            self.velocity_y += 20

        if self.velocity_y > self.gVelocity_y:
            self.velocity_y -= 20

        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.check_bounds()

    def check_bounds(self):
        min_x = 0
        min_y = 0
        max_x = 1600
        max_y = 900
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y


