import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Add player to the groups
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)

    # Create objects
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():     # makes the window's close button work
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        # Iterate over all drawables in the group and draw them
        for drawable in drawables:
            drawable.draw(screen)

        # Iterate over all updatables in the group and update them
        for updatable in updatables:
            updatable.update(dt)
        
        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        


# ensures the main() function is only called when this file is run directly, not when it's imported as a module
if __name__ == "__main__":
    main()