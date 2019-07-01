import pymunk

class Walls (pymunk.Body):
    def __init__(self, space):
        super().__init__(10, pymunk.inf)
        self.thickness = 4

        self.w1 = pymunk.Segment(space.static_body, (50,50),(50,850),self.thickness)
        self.w2 = pymunk.Segment(space.static_body, (50, 850), (1550,850), self.thickness)
        self.w3 = pymunk.Segment(space.static_body, (1550,850), (1550, 500), self.thickness)
        self.w4 = pymunk.Segment(space.static_body, (1550, 500), (400, 500), self.thickness)
        self.w5 = pymunk.Segment(space.static_body, (400, 500), (400, 400), self.thickness)
        self.w6 = pymunk.Segment(space.static_body, (400, 400), (1550, 400), self.thickness)
        self.w7 = pymunk.Segment(space.static_body, (1550, 400),(1550, 50), self.thickness)
        self.w8 = pymunk.Segment(space.static_body, (1550, 50),(50, 50), self.thickness)
        self.w9 = pymunk.Segment(space.static_body, (200,200),(200,700),self.thickness)
        self.w10 = pymunk.Segment(space.static_body, (200, 700), (1400,700), self.thickness)
        self.w11 = pymunk.Segment(space.static_body, (1400,700), (1400, 650), self.thickness)
        self.w12 = pymunk.Segment(space.static_body, (1400, 650), (250, 650), self.thickness)
        self.w13 = pymunk.Segment(space.static_body, (250, 650), (250, 250), self.thickness)
        self.w14 = pymunk.Segment(space.static_body, (250, 250), (1400, 250), self.thickness)
        self.w15 = pymunk.Segment(space.static_body, (1400, 250),(1400, 200), self.thickness)
        self.w16 = pymunk.Segment(space.static_body, (1400, 200),(200, 200), self.thickness)
        self.w1.collision_type = 2
        self.w2.collision_type = 2
        self.w3.collision_type = 2
        self.w4.collision_type = 2
        self.w5.collision_type = 2
        self.w6.collision_type = 2
        self.w7.collision_type = 2
        self.w8.collision_type = 2
        self.w9.collision_type = 2
        self.w10.collision_type = 2
        self.w11.collision_type = 2
        self.w12.collision_type = 2
        self.w13.collision_type = 2
        self.w14.collision_type = 2
        self.w15.collision_type = 2
        self.w16.collision_type = 2

        """outer edge"""
        space.add(self.w1)
        space.add(self.w2)
        space.add(self.w3)
        space.add(self.w4)
        space.add(self.w5)
        space.add(self.w6)
        space.add(self.w7)
        space.add(self.w8)

        """inner edge"""
        space.add(self.w9)
        space.add(self.w10)
        space.add(self.w11)
        space.add(self.w12)
        space.add(self.w13)
        space.add(self.w14)
        space.add(self.w15)
        space.add(self.w16)

