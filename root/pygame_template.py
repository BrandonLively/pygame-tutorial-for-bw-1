import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


#initialize Pygame and create window
pygame.init()
# allows sound
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
# allows constant fps
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    # Draw / render
    screen.fill(BLACK)
    # sets up double buffering - always doing this After drawing everything
    pygame.display.flip()

pygame.quit()