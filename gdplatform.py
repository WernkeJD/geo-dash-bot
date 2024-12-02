import pygame
import pymunk
import math

class GDPlatform():
    def __init__(self, screen, space, camera_offset, location):
        self.size = 50
        self.screen =  screen
        self.camera_offset = camera_offset
        self.location = location

        self.fail_points = [
            (0, 0),
            (0, -0.9 * self.size),
            (self.size, 0)
        ]

        self.fail_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.fail_body.position = location
        shape = pymunk.Poly(self.fail_body, self.fail_points)
        shape.collision_type = 2
        space.add(self.fail_body, shape)
        
        self.safe_points = [
            (0, -self.size),
            (self.size, -self.size),
            (self.size, 0)
        ]

        self.safe_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.safe_body.friction = 1.0
        self.safe_body.position = location
        shape = pymunk.Poly(self.safe_body, self.safe_points)
        shape.collision_type = 0
        space.add(self.safe_body, shape)

    def draw(self):
        curr_position = (self.location[0] + self.camera_offset[0], self.location[1] + self.camera_offset[1])
        self.fail_body.position = curr_position
        self.safe_body.position = curr_position

        absolute_points = (
            curr_position[0],
            curr_position[1] - self.size,
            self.size,
            self.size
        )

        pygame.draw.rect(self.screen, (255, 0, 0), absolute_points)