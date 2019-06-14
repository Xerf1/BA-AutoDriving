import pymunk

class Walls (pymunk.Body):
    def __init__(self, space):
        super().__init__(10, pymunk.inf)
        self.thickness = 4

        self.w1 = pymunk.Segment(space.static_body, (50,50),(50,850),self.thickness)
        self.w1.collision_type = 1
        """outer edge"""
        space.add(self.w1)
        space.add(pymunk.Segment(space.static_body, (50, 850), (1550,850), self.thickness))
        space.add(pymunk.Segment(space.static_body, (1550,850), (1550, 500), self.thickness))
        space.add(pymunk.Segment(space.static_body, (1550, 500), (400, 500), self.thickness))
        space.add(pymunk.Segment(space.static_body, (400, 500), (400, 400), self.thickness))
        space.add(pymunk.Segment(space.static_body, (400, 400), (1550, 400), self.thickness))
        space.add(pymunk.Segment(space.static_body, (1550, 400),(1550, 50), self.thickness))
        space.add(pymunk.Segment(space.static_body, (1550, 50),(50, 50), self.thickness))

        """inner edge"""
        space.add(pymunk.Segment(space.static_body, (200,200),(200,700),self.thickness))
        space.add(pymunk.Segment(space.static_body, (200, 700), (1400,700), self.thickness))
        space.add(pymunk.Segment(space.static_body, (1400,700), (1400, 650), self.thickness))
        space.add(pymunk.Segment(space.static_body, (1400, 650), (250, 650), self.thickness))
        space.add(pymunk.Segment(space.static_body, (250, 650), (250, 250), self.thickness))
        space.add(pymunk.Segment(space.static_body, (250, 250), (1400, 250), self.thickness))
        space.add(pymunk.Segment(space.static_body, (1400, 250),(1400, 200), self.thickness))
        space.add(pymunk.Segment(space.static_body, (1400, 200),(200, 200), self.thickness))

