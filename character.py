import pygame
import pymunk

class Character():
    size = 20

    def __init__(self, screen, space, camera_offset, location):
        self.space = space
        self.camera_offset = camera_offset

        self.x = 50
        self.y = 50

        self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 30))
        self.body.position = (self.x, self.y)
        shape = pymunk.Circle(self.body, self.size)
        shape.collision_type = 1
        space.add(self.body, shape)

        self.on_ground = False
        self.hit_object = False

        self.screen = screen

        ground_handler = space.add_collision_handler(1, 0)
        ground_handler.pre_solve = self.__begin_ground_collision
        ground_handler.separate = self.__end_ground_collision
        self.forgiveness_frames = 0

        obstacle_handler = space.add_collision_handler(1, 2)
        obstacle_handler.begin = self.__object_collision


    def draw(self):
        x, y = self.body.position
        pygame.draw.circle(self.screen, (255, 0, 0), (int(x), int(y)), self.size)


    def move(self):
        if self.forgiveness_frames > 0:
            self.forgiveness_frames -= 1
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and (self.on_ground or self.forgiveness_frames > 0):
            self.forgiveness_frames = 0
            self.body.velocity = (0, -400)

        # self.camera_offset[0] = self.body.position[0]
        # self.camera_offset[1] = self.body.position[1]
    
    def __begin_ground_collision(self, arbiter, space, data):
        self.on_ground = True
        self.forgiveness_frames = 15
        return True

    def __end_ground_collision(self, arbiter, space, data):
        self.on_ground = False
        return True
    
    def __object_collision(self, arbiter, space, data):
        self.hit_object = True
        print("HIT")
        return True