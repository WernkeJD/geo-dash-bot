import pygame
import pymunk
import math

class Obstacle():
    def __init__(self, screen, space, camera_offset, location):
        size = 60
        self.screen = screen
        self.camera_offset = camera_offset
        self.location = location

        h = math.sqrt(3) / 2 * size

        # Define points relative to the body's position
        self.points = [
            (-size / 2, 0),  # Bottom-left corner
            (size / 2, 0),   # Bottom-right corner
            (0, -h)                 # Top vertex
        ]

        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body.position = location
        shape = pymunk.Poly(self.body, self.points)
        shape.collision_type = 2
        space.add(self.body, shape)

    def draw(self):
        self.body.position = (self.location[0] + self.camera_offset[0], self.location[1] + self.camera_offset[1])

        absolute_points = [(
            p[0] + self.body.position[0],
            p[1] + self.body.position[1]
        ) for p in self.points]

        pygame.draw.polygon(self.screen, (255, 0, 0), absolute_points)
