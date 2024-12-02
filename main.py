import pygame
import sys
import pymunk
import pymunk.pygame_util

from character import Character
from obstacle import Obstacle
from gdplatform import GDPlatform

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600  # Screen dimensions
FPS = 300  # Frames per second
TITLE = "Pygame Boilerplate"

# Setup Pymunk
space = pymunk.Space()
space.gravity = (0, 900)

# Create a floor
floor = pymunk.Segment(space.static_body, (0, 500), (800, 500), 5)
floor.friction = 1.0
floor.collision_type = 0
space.add(floor)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize the mixer
pygame.mixer.init()

# Load and play background music
pygame.mixer.music.load("background_music.mp3")  # Replace with your file
pygame.mixer.music.set_volume(0.1)  # Set volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # Play on loop (-1 means infinite loop)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

draw_options = pymunk.pygame_util.DrawOptions(screen)

camera_offset = [0, 0]

# Game loop
def main():
    character = Character(screen, space, camera_offset, (0, 0))
    obstacles = []
    platforms = []

    with open('level1.txt', 'r') as f:
        data = f.readlines()

    start_offset = 500

    for row_idx, line in enumerate(data):
        for col_index, char in enumerate(line):
            if char == '1':
                platforms.append(GDPlatform(screen, space, camera_offset, (start_offset + 50 * col_index, 500 - 50 * (len(data) - row_idx - 1))))

            if char == 'X':
                obstacles.append(Obstacle(screen, space, camera_offset, (start_offset + 50 * col_index, 500 - 50 * (len(data) - row_idx - 1))))
            
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic
        space.step(1/FPS)

        # Drawing
        screen.fill(BLACK)  # Clear the screen with a black color
        
        character.move()
        character.draw()

        for indx, obstacle in enumerate(obstacles):
            obstacle.draw()

            # if indx == len(obstacles - 1):
            #     break

        for platform in platforms:
            platform.draw()

        # Draw the floor in green
        pygame.draw.line(screen, GREEN,  (0, 600), (800, 600), 210)

        
        # Use debug_draw for other objects
        space.debug_draw(draw_options)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)
        camera_offset[0] -= 120/FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

