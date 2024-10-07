import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():     # makes the window's close button work
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)
        pygame.display.flip()


# ensures the main() function is only called when this file is run directly, not when it's imported as a module
if __name__ == "__main__":
    main()