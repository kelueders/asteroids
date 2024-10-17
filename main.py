import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add player to the groups
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    Shot.containers = (shots, updatables, drawables)

    # Create objects
    asteroidfield = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

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

        # Iterate over all asteroids in the group and check for collision with both player and shots
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.split()
        
        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        


# ensures the main() function is only called when this file is run directly, not when it's imported as a module
if __name__ == "__main__":
    main()