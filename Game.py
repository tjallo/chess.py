import pygame
from pygame import draw
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


def run() -> None:
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    
    while running:

        # Look at every event in the queue

        for event in pygame.event.get():

            # Did the user hit a key?

            if event.type == KEYDOWN:

                # Was it the Escape key? If so, stop the loop.

                if event.key == K_ESCAPE:

                    running = False

            # Did the user click the window close button? If so, stop the loop.

            elif event.type == QUIT:

                running = False
    
