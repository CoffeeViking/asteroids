import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update Objects
        updatable.update(dt)
        
        #Check For Collisions
        for ast in asteroids:
            if ast.collision_check(player):
                sys.exit("Game Over!")

        # Draw Background then Drawables
        screen.fill("black")
        for item in drawable:
            item.draw(screen)

        #Move time along
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
